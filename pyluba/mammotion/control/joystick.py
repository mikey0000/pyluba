import asyncio
from timeit import default_timer as timer

import nest_asyncio
import pyjoystick
from pyjoystick.sdl2 import Key, run_event_loop
from pyjoystick.utils import PeriodicThread

from pyluba import MammotionBaseBLEDevice
from pyluba.event import BleNotificationEvent
from pyluba.utility.rocker_util import RockerControlUtil

bleNotificationEvt = BleNotificationEvent()

nest_asyncio.apply()


class JoystickControl:
    """Joystick class for controlling Luba with a joystick"""

    angular_percent = 0
    linear_percent = 0
    linear_speed = 0
    angular_speed = 0
    ignore_events = False
    _blade_height = 25
    worker = None

    def __init__(self, luba_ble: MammotionBaseBLEDevice):
        self._client = luba_ble
        self._curr_time = timer()
        self.stopped = False

        repeater = pyjoystick.HatRepeater(
            first_repeat_timeout=0.2, repeat_timeout=0.03, check_timeout=0.01
        )

        self.mngr = pyjoystick.ThreadEventManager(
            event_loop=run_event_loop,
            handle_key_event=self.key_received,
            add_joystick=self.print_add,
            remove_joystick=self.print_remove,
            button_repeater=repeater,
        )

        self.worker = PeriodicThread(
            0.2, self.run_movement, name="luba-process_movements"
        )
        self.worker.alive = self.mngr.alive  # stop when this event stops
        self.worker.daemon = True

    def _movement_finished(self):
        self.ignore_events = False

    def run_movement(self):
        if self.linear_percent == 0.0 and self.angular_percent == 0.0:
            if self.stopped:
                return
            self.stopped = True
        self.stopped = False
        (linear_speed, angular_speed) = self.transform_both_speeds(
            self.linear_speed,
            self.angular_speed,
            self.linear_percent,
            self.angular_percent,
        )
        asyncio.run(
            self._client.command(
                "send_movement", linear_speed=linear_speed, angular_speed=angular_speed
            )
        )

    def print_add(self, joy):
        print("Added", joy)

    def print_remove(self, joy):
        print("Removed", joy)

    def key_received(self, key):
        self.handle_key_received(key)

    def run_controller(self):
        self.mngr.start()
        self.worker.start()

    def get_percent(self, percent: float):
        if percent <= 15.0:
            return 0.0

        return percent - 15.0

    @staticmethod
    def transform_both_speeds(
        linear: float, angular: float, linear_percent: float, angular_percent: float
    ):
        transfrom3 = RockerControlUtil.getInstance().transfrom3(linear, linear_percent)
        transform4 = RockerControlUtil.getInstance().transfrom3(
            angular, angular_percent
        )

        if transfrom3 is not None and len(transfrom3) > 0:
            linear_speed = transfrom3[0] * 10
            angular_speed = int(transform4[1] * 4.5)
            print(linear_speed, angular_speed)
            return linear_speed, angular_speed

    def handle_key_received(self, key):
        # print(key, "-", key.keytype, "-", key.number, "-", key.value)

        if key.keytype is Key.BUTTON and key.value == 1:
            # print(key, "-", key.keytype, "-", key.number, "-", key.value)
            if key.number == 0:  # x
                asyncio.run(self._client.command("return_to_dock"))
            if key.number == 1:
                asyncio.run(self._client.command("leave_dock"))
            if key.number == 3:
                asyncio.run(self._client.command("set_blade_control", on_off=1))
            if key.number == 2:
                asyncio.run(self._client.command("set_blade_control", on_off=0))
            if key.number == 9:
                # lower knife height
                if self._blade_height > 25:
                    self._blade_height -= 5
                    asyncio.run(
                        self._client.command(
                            "set_blade_height", height=self._blade_height
                        )
                    )
            if key.number == 10:
                # raise knife height
                if self._blade_height < 60:
                    self._blade_height += 5
                    asyncio.run(
                        self._client.command(
                            "set_blade_height", height=self._blade_height
                        )
                    )

        if key.keytype is Key.AXIS:
            # print(key, "-", key.keytype, "-", key.number, "-", key.value)
            if key.value > 0.09 or key.value < -0.09:
                match key.number:
                    case 1:  # left (up down)
                        # take left right values and convert to linear movement
                        # -1 is forward
                        # 1 is back

                        # linear_speed==1000
                        # linear_speed==-1000
                        print("case 1")
                        if key.value > 0:
                            self.linear_speed = 270.0
                            self.linear_percent = self.get_percent(abs(key.value * 100))
                        else:
                            self.linear_speed = 90.0
                            self.linear_percent = self.get_percent(abs(key.value * 100))

                    case 2:  # right  (left right)
                        # take left right values and convert to angular movement
                        # -1 left
                        # 1 is right
                        # angular_speed==-450
                        # angular_speed==450
                        if key.value > 0:
                            self.angular_speed = 0.0
                            self.angular_percent = self.get_percent(
                                abs(key.value * 100)
                            )
                        else:
                            # angle=180.0
                            # linear_speed=0//angular_speed=-450
                            self.angular_speed = 180.0
                            self.angular_percent = self.get_percent(
                                abs(key.value * 100)
                            )

            else:
                match key.number:
                    case 1:  # left (up down)
                        self.linear_speed = 0.0
                        self.linear_percent = 0.0
                    case 2:  # right  (left right)
                        self.angular_speed = 0.0
                        self.angular_percent = 0.0
