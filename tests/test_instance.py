import asyncio
from threading import Thread
import threading
from luba_desktop.ble_connection import BleLubaConnection
from luba_desktop.control.joystick_control import JoystickControl
from luba_desktop.blufi_impl import Blufi
from luba_desktop.blelibs.notifydata import BlufiNotifyData
from luba_desktop.event.event import BleNotificationEvent, MoveEvent

address = "90:38:0C:6E:EE:9E"
UUID_SERVICE = "0000ffff-0000-1000-8000-00805f9b34fb"
UUID_WRITE_CHARACTERISTIC = "0000ff01-0000-1000-8000-00805f9b34fb"
UUID_NOTIFICATION_CHARACTERISTIC = "0000ff02-0000-1000-8000-00805f9b34fb"
UUID_NOTIFICATION_DESCRIPTOR = "00002902-0000-1000-8000-00805f9b34fb"

CLIENT_CHARACTERISTIC_CONFIG_DESCRIPTOR_UUID = "00002902-0000-1000-8000-00805f9b34fb"
BATTERY_SERVICE = "0000180F-0000-1000-8000-00805f9b34fb"
BATTERY_LEVEL_CHARACTERISTIC = "00002A19-0000-1000-8000-00805f9b34fb"
GENERIC_ATTRIBUTE_SERVICE = "00001801-0000-1000-8000-00805f9b34fb"
SERVICE_CHANGED_CHARACTERISTIC = "00002A05-0000-1000-8000-00805f9b34fb"
moveEvt = MoveEvent()
bleNotificationEvt = BleNotificationEvent()


async def ble_heartbeat(blufi_client):
    while True:
        await blufi_client.sendTodevBleSync()
        # eventually send an event and update data from sync
        await asyncio.sleep(15)

class AsyncLoopThread(Thread):
    def __init__(self):
        super().__init__(daemon=True)
        self.loop = asyncio.new_event_loop()

    def run(self):
        asyncio.set_event_loop(self.loop)
        self.loop.run_forever()


async def run():
    bleLubaConn = BleLubaConnection(bleNotificationEvt)
    await bleLubaConn.scanForLubaAndConnect()
    await bleLubaConn.notifications()
    client = bleLubaConn.getClient()
    blufi_client = Blufi(client, moveEvt)

    def handleNotifications(data:bytearray):
        notification = BlufiNotifyData()
        result = blufi_client.parseNotification(data, notification)
        blufi_client.parseBlufiNotifyData(notification)
        print(result)
        print(notification)

    bleNotificationEvt.AddSubscribersForBleNotificationEvent(handleNotifications)
    # Run the ble heart beat in the background continuously which still doesn't quite work
    loop_handler_bleheart = AsyncLoopThread()
    loop_handler_bleheart.start()
    asyncio.run_coroutine_threadsafe(ble_heartbeat(blufi_client), loop_handler_bleheart.loop)
    
    print("joystick code")
    in_queue = asyncio.Queue()
    joystick = JoystickControl().controller(blufi_client, moveEvt)
    # no idea if this will work but might
    joy_input_thread = threading.Thread(target=joystick.run_controller, args=(), daemon=True)
    joy_input_thread.start()

    print("end run?")
	#await main(address, UUID_NOTIFICATION_CHARACTERISTIC,moveEvt)



if __name__ ==  '__main__':
    event_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(event_loop)
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(run())
    # 
    # asyncio.run(run())
    event_loop.run_until_complete(run())
    
    # asyncio.ensure_future(function_2())
    # loop.run_forever()
    

