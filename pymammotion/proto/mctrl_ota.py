# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: pymammotion/proto/mctrl_ota.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


class InfoType(betterproto.Enum):
    IT_BASE = 0
    IT_OTA = 1


@dataclass
class BaseInfo(betterproto.Message):
    dev_version: str = betterproto.string_field(1)
    dev_status: int = betterproto.int32_field(2)
    batt_val: int = betterproto.int32_field(3)
    init_status: int = betterproto.int32_field(4)
    is_tilt: int = betterproto.int32_field(5)


@dataclass
class OtaInfo(betterproto.Message):
    otaid: str = betterproto.string_field(1)
    version: str = betterproto.string_field(2)
    progress: int = betterproto.int32_field(3)
    result: int = betterproto.int32_field(4)
    message: str = betterproto.string_field(5)


@dataclass
class GetInfoReq(betterproto.Message):
    type: "InfoType" = betterproto.enum_field(1)


@dataclass
class GetInfoRsp(betterproto.Message):
    result: int = betterproto.int32_field(1)
    type: "InfoType" = betterproto.enum_field(2)
    base: "BaseInfo" = betterproto.message_field(3, group="info")
    ota: "OtaInfo" = betterproto.message_field(4, group="info")


@dataclass
class MctlOta(betterproto.Message):
    todev_get_info_req: "GetInfoReq" = betterproto.message_field(1, group="SubOtaMsg")
    toapp_get_info_rsp: "GetInfoRsp" = betterproto.message_field(2, group="SubOtaMsg")
