# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pyluba/proto/dev_net.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1apyluba/proto/dev_net.proto\"\x83\x06\n\x06\x44\x65vNet\x12\x18\n\x0etodev_ble_sync\x18\x01 \x01(\x05H\x00\x12\x18\n\x0etodev_ConfType\x18\x02 \x01(\x05H\x00\x12-\n\x13todev_wifimsgupload\x18\x03 \x01(\x0b\x32\x0e.DrvWifiUploadH\x00\x12+\n\x14todev_wifilistupload\x18\x04 \x01(\x0b\x32\x0b.DrvWifiSetH\x00\x12/\n\x18todev_wifi_configuration\x18\x05 \x01(\x0b\x32\x0b.DrvWifiSetH\x00\x12$\n\rtoapp_wifimsg\x18\x06 \x01(\x0b\x32\x0b.DrvWifiMsgH\x00\x12&\n\x0etoapp_WifiConf\x18\x07 \x01(\x0b\x32\x0c.DrvWifiConfH\x00\x12*\n\x10toapp_ListUpload\x18\x08 \x01(\x0b\x32\x0e.DrvListUploadH\x00\x12\x1c\n\x12todev_req_log_info\x18\t \x01(\x05H\x00\x12\x35\n\x15todev_log_data_cancel\x18\n \x01(\x0b\x32\x14.DrvUploadFileCancelH\x00\x12+\n\x11todev_devinfo_req\x18\x0b \x01(\x0b\x32\x0e.DrvDevInfoReqH\x00\x12-\n\x12toapp_devinfo_resp\x18\x0c \x01(\x0b\x32\x0f.DrvDevInfoRespH\x00\x12\x1e\n\x14toapp_upgrade_report\x18\r \x01(\x05H\x00\x12\x35\n\x15toapp_wifi_iot_status\x18\x0e \x01(\x0b\x32\x14.WifiIotStatusReportH\x00\x12\x1e\n\x14todev_uploadfile_req\x18\x0f \x01(\x05H\x00\x12\x1e\n\x14toapp_uploadfile_rsp\x18\x10 \x01(\x05H\x00\x12\x33\n\x15todev_networkinfo_req\x18\x11 \x01(\x0b\x32\x12.GetNetworkInfoReqH\x00\x12\x33\n\x15toapp_networkinfo_rsp\x18\x12 \x01(\x0b\x32\x12.GetNetworkInfoRspH\x00\x42\x0c\n\nNetSubType\"\\\n\rDrvListUpload\x12\x0f\n\x07\x63urrent\x18\x02 \x01(\x05\x12\x0b\n\x03sum\x18\x01 \x01(\x05\x12\x0c\n\x04rssi\x18\x05 \x01(\x05\x12\x0e\n\x06status\x18\x03 \x01(\x05\x12\x0f\n\x07memssid\x18\x04 \x01(\t\"&\n\rDrvWifiUpload\x12\x15\n\rwifiMsgUpload\x18\x01 \x01(\x05\"$\n\x0b\x44rvWifiList\x12\x15\n\rnVSWifiUpload\x18\x01 \x01(\x05\"\x93\x01\n\nDrvWifiMsg\x12\x0f\n\x07status1\x18\x01 \x01(\t\x12\x0f\n\x07status2\x18\x02 \x01(\t\x12\n\n\x02iP\x18\x03 \x01(\t\x12\x0f\n\x07msgssid\x18\x04 \x01(\t\x12\x10\n\x08password\x18\x05 \x01(\t\x12\x0c\n\x04rssi\x18\x06 \x01(\x05\x12\x12\n\nproductkey\x18\x07 \x01(\t\x12\x12\n\ndevicename\x18\x08 \x01(\t\"3\n\nDrvWifiSet\x12\x13\n\x0b\x63onfigParam\x18\x01 \x01(\x05\x12\x10\n\x08\x63onfSsid\x18\x02 \x01(\t\"?\n\x0b\x44rvWifiConf\x12\x10\n\x08succFlag\x18\x01 \x01(\x08\x12\x0c\n\x04\x63ode\x18\x02 \x01(\x05\x12\x10\n\x08\x63onfssid\x18\x03 \x01(\t\"+\n\x0f\x44rvDevInfoReqId\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04type\x18\x02 \x01(\x05\"G\n\x10\x44rvDevInfoRespId\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04type\x18\x02 \x01(\x05\x12\x0c\n\x04info\x18\x03 \x01(\t\x12\x0b\n\x03res\x18\x04 \x01(\x05\"2\n\rDrvDevInfoReq\x12!\n\x07req_ids\x18\x01 \x03(\x0b\x32\x10.DrvDevInfoReqId\"5\n\x0e\x44rvDevInfoResp\x12#\n\x08resp_ids\x18\x01 \x03(\x0b\x32\x11.DrvDevInfoRespId\"l\n\x13WifiIotStatusReport\x12\x16\n\x0ewifi_connected\x18\x01 \x01(\x08\x12\x15\n\riot_connected\x18\x02 \x01(\x08\x12\x12\n\nproductkey\x18\x03 \x01(\t\x12\x12\n\ndevicename\x18\x04 \x01(\t\"\xdd\x01\n\x15\x44rvUploadFileToAppReq\x12\x12\n\x05\x62izId\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x16\n\toperation\x18\x02 \x01(\x05H\x01\x88\x01\x01\x12\x15\n\x08serverIp\x18\x03 \x01(\x05H\x02\x88\x01\x01\x12\x17\n\nserverPort\x18\x04 \x01(\x05H\x03\x88\x01\x01\x12\x10\n\x03num\x18\x05 \x01(\x05H\x04\x88\x01\x01\x12\x11\n\x04type\x18\x06 \x01(\x05H\x05\x88\x01\x01\x42\x08\n\x06_bizIdB\x0c\n\n_operationB\x0b\n\t_serverIpB\r\n\x0b_serverPortB\x06\n\x04_numB\x07\n\x05_type\"$\n\x11GetNetworkInfoReq\x12\x0f\n\x07req_ids\x18\x01 \x01(\x05\"\x87\x01\n\x11GetNetworkInfoRsp\x12\x0f\n\x07req_ids\x18\x01 \x01(\x05\x12\x11\n\twifi_ssid\x18\x02 \x01(\t\x12\x10\n\x08wifi_mac\x18\x03 \x01(\t\x12\x11\n\twifi_rssi\x18\x04 \x01(\x05\x12\n\n\x02ip\x18\x05 \x01(\x05\x12\x0c\n\x04mask\x18\x06 \x01(\x05\x12\x0f\n\x07gateway\x18\x07 \x01(\x05\"$\n\x13\x44rvUploadFileCancel\x12\r\n\x05\x62izId\x18\x01 \x01(\x05*\\\n\x0cWifiConfType\x12\x12\n\x0e\x44isconnectWifi\x10\x00\x12\x0e\n\nForgetWifi\x10\x01\x12\x15\n\x11\x44irectConnectWifi\x10\x02\x12\x11\n\rReconnectWifi\x10\x03*R\n\x10\x44rvDevInfoResult\x12\x13\n\x0f\x44RV_RESULT_FAIL\x10\x00\x12\x12\n\x0e\x44RV_RESULT_SUC\x10\x01\x12\x15\n\x11\x44RV_RESULT_NOTSUP\x10\x02\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pyluba.proto.dev_net_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _WIFICONFTYPE._serialized_start=2017
  _WIFICONFTYPE._serialized_end=2109
  _DRVDEVINFORESULT._serialized_start=2111
  _DRVDEVINFORESULT._serialized_end=2193
  _DEVNET._serialized_start=31
  _DEVNET._serialized_end=802
  _DRVLISTUPLOAD._serialized_start=804
  _DRVLISTUPLOAD._serialized_end=896
  _DRVWIFIUPLOAD._serialized_start=898
  _DRVWIFIUPLOAD._serialized_end=936
  _DRVWIFILIST._serialized_start=938
  _DRVWIFILIST._serialized_end=974
  _DRVWIFIMSG._serialized_start=977
  _DRVWIFIMSG._serialized_end=1124
  _DRVWIFISET._serialized_start=1126
  _DRVWIFISET._serialized_end=1177
  _DRVWIFICONF._serialized_start=1179
  _DRVWIFICONF._serialized_end=1242
  _DRVDEVINFOREQID._serialized_start=1244
  _DRVDEVINFOREQID._serialized_end=1287
  _DRVDEVINFORESPID._serialized_start=1289
  _DRVDEVINFORESPID._serialized_end=1360
  _DRVDEVINFOREQ._serialized_start=1362
  _DRVDEVINFOREQ._serialized_end=1412
  _DRVDEVINFORESP._serialized_start=1414
  _DRVDEVINFORESP._serialized_end=1467
  _WIFIIOTSTATUSREPORT._serialized_start=1469
  _WIFIIOTSTATUSREPORT._serialized_end=1577
  _DRVUPLOADFILETOAPPREQ._serialized_start=1580
  _DRVUPLOADFILETOAPPREQ._serialized_end=1801
  _GETNETWORKINFOREQ._serialized_start=1803
  _GETNETWORKINFOREQ._serialized_end=1839
  _GETNETWORKINFORSP._serialized_start=1842
  _GETNETWORKINFORSP._serialized_end=1977
  _DRVUPLOADFILECANCEL._serialized_start=1979
  _DRVUPLOADFILECANCEL._serialized_end=2015
# @@protoc_insertion_point(module_scope)
