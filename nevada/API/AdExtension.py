from nevada.Common.Connector import *
from typing import List
import jsonpickle
import json

class CreateAdExtensionObject:
    def __init__(self, pcChannelId, mobileChannelId, ownerId, type, userLock):
        self.pcChannelId = pcChannelId
        self.mobileChannelId = mobileChannelId
        self.ownerId = ownerId
        self.schedule = None
        self.type = type
        self.userLock = userLock

class UpdateAdExtensionObject:
    def __init__(self, nccAdExtensionId, schedule=None, userLock = None):
        self.nccAdExtensionId = nccAdExtensionId
        self.schedule = schedule
        self.userLock = userLock

class AdExtensionObject:
    def __init__(self, json_def):
        if type(json_def) is str:
            json_def = json.loads(json_def)
        s = json_def
        self.customerId = None if 'customerId' not in s else s['customerId']
        self.delFlag = None if 'delFlag' not in s else s['delFlag']
        self.editTm = None if 'editTm' not in s else s['editTm']
        self.inspectStatus = None if 'inspectStatus' not in s else s['inspectStatus']
        self.mobileChannelId = None if 'mobileChannelId' not in s else s['mobileChannelId']
        self.nccAdExtensionId = None if 'nccAdExtensionId' not in s else s['nccAdExtensionId']
        self.ownerId = None if 'ownerId' not in s else s['ownerId']
        self.pcChannelId = None if 'pcChannelId' not in s else s['pcChannelId']
        self.regTm = None if 'regTm' not in s else s['regTm']
        self.status = None if 'status' not in s else s['status']
        self.statusReason = None if 'statusReason' not in s else s['statusReason']
        self.type = None if 'type' not in s else s['type']
        self.userLock = None if 'userLock' not in s else s['userLock']


class AdExtension:  # 확장소재
    def __init__(self, base_url: str, api_key: str, secret_key: str, customer_id: int):
        self.conn = Connector(base_url, api_key, secret_key, customer_id)
    AdExtensionObjectList = List[AdExtensionObject]
    IdList = List[str]
    ChangeFieldsList = List[str]

    def get_ad_extensions_list(self, ownerId: str) -> AdExtensionObjectList:
        result = self.conn.get('/ncc/ad-extensions', {'ownerId': ownerId})
        adext_list = []
        for arr in result:
            camp = AdExtensionObject(arr)
            adext_list.append(camp)
        return adext_list

    def get_ad_extensions_list_by_ids(self, ids: IdList) -> AdExtensionObjectList:
        ids = ",".join(ids)
        ids = {'ids': ids}
        result = self.conn.get('/ncc/ad-extensions', ids)
        adext_list = []
        for arr in result:
            camp = AdExtensionObject(arr)
            adext_list.append(camp)
        return adext_list

    def get_ad_extensions(self, adExtensionId: str) -> AdExtensionObject:
        result = self.conn.get('/ncc/ad-extensions/' + adExtensionId)
        result = AdExtensionObject(result)

        return result

    def create_ad_extensions(self, CreateAdExtensionObject: CreateAdExtensionObject) -> AdExtensionObject:
        data = jsonpickle.encode(CreateAdExtensionObject, unpicklable=False)
        data = json.loads(data)
        data = CommonFunctions.dropna(data)
        data_str = data
        data_str = json.dumps(data_str)

        result = self.conn.post('/ncc/ad-extensions', data_str)
        result = AdExtensionObject(result)
        return result

    def update_ad_extensions(self, adExtensionId: str, fields: ChangeFieldsList,
                             UpdateAdExtensionObject: UpdateAdExtensionObject) -> AdExtensionObject:
        data = jsonpickle.encode(UpdateAdExtensionObject, unpicklable=False)
        data = json.loads(data)
        data = CommonFunctions.dropna(data)
        data_str = data
        data_str = json.dumps(data_str)
        change_fields_list = ",".join(fields)
        query = {'fields': change_fields_list}
        result = self.conn.put('/ncc/ad-extensions/' + adExtensionId, data_str, query)
        result = AdExtensionObject(result)
        return result

    def delete_ad_extensions(self, adExtensionId: str):
        self.conn.delete('/ncc/ad-extensions/' + adExtensionId)
        return True
