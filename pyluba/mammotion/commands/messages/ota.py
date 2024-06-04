# === sendOrderMsg_Ota ===
from pyluba.proto import luba_msg_pb2, mctrl_ota_pb2


def send_order_msg_ota(self, ota):
    luba_msg = luba_msg_pb2.LubaMsg(
        msgtype=luba_msg_pb2.MsgCmdType.MSG_CMD_TYPE_EMBED_OTA,
        sender=luba_msg_pb2.MsgDevice.DEV_MOBILEAPP,
        rcver=luba_msg_pb2.MsgDevice.DEV_MAINCTL,
        msgattr=luba_msg_pb2.MsgAttr.MSG_ATTR_REQ,
        seqs=1,
        version=1,
        subtype=1,
        ota=ota)

    return luba_msg.SerializeToString()


def get_device_ota_info(self, log_type: int):
    todev_get_info_req = mctrl_ota_pb2.MctlOta(
        todev_get_info_req=mctrl_ota_pb2.getInfoReq(
            type=mctrl_ota_pb2.IT_OTA
        )
    )

    print("===Send command to get upgrade details===logType:" + str(log_type))
    return self.send_order_msg_ota(todev_get_info_req)


def get_device_info_new(self):
    """New device call for OTA upgrade information."""
    todev_get_info_req = mctrl_ota_pb2.MctlOta(
        todev_get_info_req=mctrl_ota_pb2.getInfoReq(
            type=mctrl_ota_pb2.IT_BASE
        )
    )
    print("Send to get OTA upgrade information", "Get device information")
    return self.send_order_msg_ota(todev_get_info_req)