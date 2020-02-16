from nevada.Common.Connector import *
from typing import List
import jsonpickle
import json

class BusinessInfo:
    def __init__(self, json_def):
        if type(json_def) is str:
            json_def = json.loads(json_def)
        s = json_def
        self.isMobileNaverLogin = None if 'isMobileNaverLogin' not in s else s['isMobileNaverLogin']
        self.isMobileNaverPay = None if 'isMobileNaverPay' not in s else s['isMobileNaverPay']
        self.isMobileNaverTalkTalk = None if 'isMobileNaverTalkTalk' not in s else s['isMobileNaverTalkTalk']
        self.isNaverLogin = None if 'isNaverLogin' not in s else s['isNaverLogin']
        self.isNaverPay = None if 'isNaverPay' not in s else s['isNaverPay']
        self.isNaverTalkTalk = None if 'isNaverTalkTalk' not in s else s['isNaverTalkTalk']
        self.isStoreFarm = None if 'isStoreFarm' not in s else s['isStoreFarm']
        self.mobileCertStatus = None if 'mobileCertStatus' not in s else s['mobileCertStatus']
        self.naAccountId = None if 'naAccountId' not in s else s['naAccountId']
        self.naAccountType = None if 'naAccountType' not in s else s['naAccountType']
        self.originalPath = None if 'originalPath' not in s else s['originalPath']
        self.site = None if 'site' not in s else s['site']
        self.thumbnailPath = None if 'thumbnailPath' not in s else s['thumbnailPath']
        self.useNaverPayNaScript = None if 'useNaverPayNaScript' not in s else s['useNaverPayNaScript']
        self.useSaNaScript = None if 'useSaNaScript' not in s else s['useSaNaScript']
        self.useStoreFarmNaScript = None if 'useStoreFarmNaScript' not in s else s['useStoreFarmNaScript']

class UpdateBusinessChannelObject:
    def __init__(self, nccBusinessChannelId, site_url, name):
        self.businessInfo = {'site' : site_url}
        self.channelTp = 'SITE'
        self.inspectRequestMsg = None
        self.name = name
        self.nccBusinessChannelId = nccBusinessChannelId

class CreateBusinessChannelObject:
    def __init__(self, businessInfo, channelTp, name, inspectReqeustMsg=None):
        self.businessInfo = businessInfo#{'site':'github.com/taegyumin'}#
        self.channelTp = channelTp
        self.inspectRequestMsg = inspectReqeustMsg
        self.name = name

class BusinessChannelObject:
    def __init__(self, json_def):
        if type(json_def) is str:
            json_def = json.loads(json_def)
        s = json_def
        self.adultStatus = None if 'adultStatus' not in s else s['adultStatus']
        self.blackStatus = None if 'blackStatus' not in s else s['blackStatus']
        self.businessInfo = None if 'businessInfo' not in s else BusinessInfo(s['businessInfo'])
        self.channelKey = None if 'channelKey' not in s else s['channelKey']
        self.channelTp = None if 'channelTp' not in s else s['channelTp']
        self.customerId = None if 'customerId' not in s else s['customerId']
        self.delFlag = None if 'delFlag' not in s else s['delFlag']
        self.editTm = None if 'editTm' not in s else s['editTm']
        self.enabled = None if 'enabled' not in s else s['enabled']
        self.firstChargeTm = None if 'firstChargeTm' not in s else s['firstChargeTm']
        self.inspectTm = None if 'inspectTm' not in s else s['inspectTm']
        self.mobileInspectStatus = None if 'mobileInspectStatus' not in s else s['mobileInspectStatus']
        self.name = None if 'name' not in s else s['name']
        self.nccBusinessChannelId = None if 'nccBusinessChannelId' not in s else s['nccBusinessChannelId']
        self.pcInspectStatus = None if 'pcInspectStatus' not in s else s['pcInspectStatus']
        self.regTm = None if 'regTm' not in s else s['regTm']
        self.status = None if 'status' not in s else s['status']
        self.statusReason = None if 'statusReason' not in s else s['statusReason']


class BusinessChannel:
    def __init__(self, base_url: str, api_key: str, secret_key: str, customer_id: int):
        self.conn = Connector(base_url, api_key, secret_key, customer_id)

    BusinessChannelObjectList = List[BusinessChannelObject]
    BusinessChannelIdList = List[str]

    def get_business_channel_json(self, businessChannelId: str):
        result = self.conn.get('/ncc/channels/' + businessChannelId)
        return result

    def get_business_channel_list(self, businessChannelId: str) -> BusinessChannelObject:
        result = self.get_business_channel_json(businessChannelId)
        result = BusinessChannelObject(result)
        return result

    def get_business_channel_all_json(self):
        result = self.conn.get('/ncc/channels')
        return result

    def get_business_channel_all_list(self) -> BusinessChannelObjectList:
        result = self.get_business_channel_all_json()
        business_channel_list = []
        for arr in result:
            channel = BusinessChannelObject(arr)
            business_channel_list.append(channel)
        return business_channel_list

    def get_business_channel_by_type_json(self, channelTp: str):
        result = self.conn.get('/ncc/channels', {'channelTp': channelTp})
        return result

    def get_business_channel_by_type_list(self, channelTp: str) -> BusinessChannelObjectList:
        result = self.get_business_channel_by_type_json(channelTp)
        business_channel_list = []
        for arr in result:
            channel = BusinessChannelObject(arr)
            business_channel_list.append(channel)
        return business_channel_list

    def get_business_channel_by_ids_json(self, ids: BusinessChannelIdList):
        ids = ",".join(ids)
        query = {'ids': ids}
        result = self.conn.get('/ncc/channels', query)
        return result

    def get_business_channel_by_ids_list(self, ids: BusinessChannelIdList) -> BusinessChannelObjectList:
        result = self.get_business_channel_by_ids_json(ids)
        business_channel_list = []
        for arr in result:
            channel = BusinessChannelObject(arr)
            business_channel_list.append(channel)
        return business_channel_list

    def create_business_channel(self, CreateBusinessChannelObject: CreateBusinessChannelObject) -> BusinessChannelObject:
        data = jsonpickle.encode(CreateBusinessChannelObject, unpicklable=False)
        data = json.loads(data)
        data = CommonFunctions.dropna(data)
        data_str = json.dumps(data)
        result = self.conn.post('/ncc/channels', data_str)
        result = BusinessChannelObject(result)
        return result

    def update_business_channel(self, fields,
                                UpdateBusinessChannelObject: UpdateBusinessChannelObject) -> BusinessChannelObject:
        data = jsonpickle.encode(UpdateBusinessChannelObject, unpicklable=False)
        data = json.loads(data)
        data = CommonFunctions.dropna(data)
        data_str = json.dumps(data)
        result = self.conn.put('/ncc/channels', data_str, fields)
        result = BusinessChannelObject(result)
        return result

    def delete_business_channel(self, businessChannelId: str):
        self.conn.delete('/ncc/channels/' + businessChannelId)
        return True

    def delete_business_channel_by_ids(self, ids: BusinessChannelIdList):
        ids = ",".join(ids)
        query = {'ids': ids}
        self.conn.delete('/ncc/channels', query)
        return True