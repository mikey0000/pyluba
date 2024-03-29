from typing import Dict

from google.protobuf.message import DecodeError
from pyluba.proto import mctrl_driver_pb2, luba_msg_pb2, esp_driver_pb2, mctrl_nav_pb2, mctrl_sys_pb2
from pyluba.data.model import HashList, RegionData

# until we have a proper store or send messages somewhere
device_charge_map: Dict[str, int] = {}
deviceRtkStatusMap: Dict[str, int] = {}
deviceSelfCheckFlagMap: Dict[str, bool] = {}
devicePileMap: Dict[str, int] = {}
devicePosTypeMap: Dict[str, int] = {}
device_state_map: Dict[str, int] = {}
deviceBreakPointMap: Dict[str, int] = {}
chargeStateTemp = -1


'''Parse data packets back into their protobuf types.

TODO allow for registering events to individual messages
as trying to register for all would be a mess
'''
def parseCustomData(data: bytearray):
    # pass
    # print(data)
    # setReceiveDeviceData
    
    
    
    luba_msg = luba_msg_pb2.LubaMsg()
    try:
        luba_msg.ParseFromString(data)
        # print(luba_msg)
        
        # toappGetHashAck = luba_msg.nav.toapp_get_commondata_ack
        # print(toappGetHashAck.Hash)
        
        if(luba_msg.HasField('sys')):
            store_sys_data(luba_msg.sys)
        elif(luba_msg.HasField('esp')):
            store_esp_data(luba_msg.esp)
        elif(luba_msg.HasField('nav')):
            store_nav_data(luba_msg.nav)
        elif(luba_msg.HasField('driver')):
            pass
        else:
            pass
        
    except DecodeError as err:
        print(err)
        
        
def store_sys_data(sys):
    if(sys.HasField("system_tard_state_tunnel")):
        tardStateDataList = sys.system_tard_state_tunnel.tard_state_data
        longValue8 = tardStateDataList[0]
        longValue9 = tardStateDataList[1]
        print("Device status report,deviceState:", longValue8, ",deviceName:", "Luba...")
        chargeStateTemp = longValue9
        longValue10 = tardStateDataList[6]
        longValue11 = tardStateDataList[7]

        #device_state_map        

        
        
def store_nav_data(nav):
    if(nav.HasField('toapp_get_commondata_ack')):
        """has data about paths and zones"""   
        toapp_get_commondata_ack = nav.toapp_get_commondata_ack
        region_data = RegionData()
        region_data.result = toapp_get_commondata_ack.result
        region_data.action = toapp_get_commondata_ack.action
        region_data.type = toapp_get_commondata_ack.type
        region_data.Hash = toapp_get_commondata_ack.Hash
        region_data.pHashA = int(toapp_get_commondata_ack.paternalHashA)
        region_data.pHashB = int(toapp_get_commondata_ack.paternalHashB)
        region_data.path = toapp_get_commondata_ack.dataCouple
        region_data.subCmd = toapp_get_commondata_ack.subCmd
        region_data.totalFrame = toapp_get_commondata_ack.totalFrame
        region_data.currentFrame = toapp_get_commondata_ack.currentFrame
        region_data.dataHash = toapp_get_commondata_ack.dataHash
        region_data.dataLen = toapp_get_commondata_ack.dataLen
        region_data.pver = toapp_get_commondata_ack.pver
        print(region_data)

    
    if(nav.HasField('toapp_gethash_ack')):
        toapp_gethash_ack = nav.toapp_gethash_ack
        # luba.nav.toapp_get_commondata_ack.DESCRIPTOR.fields_by_name
        hash_list = HashList()

        dataCoupleList = toapp_gethash_ack.dataCouple
        hash_list.pver = toapp_gethash_ack.pver
        hash_list.subCmd = toapp_gethash_ack.subCmd
        hash_list.currentFrame = toapp_gethash_ack.currentFrame
        hash_list.totalFrame = toapp_gethash_ack.totalFrame
        hash_list.dataHash = int(toapp_gethash_ack.dataHash)
        hash_list.path = dataCoupleList
        print(hash_list)
        # use callback to provide hash list
    
def store_esp_data(esp):
    if(esp.toapp_wifi_iot_status):
        iot_status = esp.toapp_wifi_iot_status
        print(iot_status.devicename)