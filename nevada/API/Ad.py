from nevada.Common.Connector import *
from typing import List
import jsonpickle
import json

class AdFieldObject:
    def __init__(self, json_def=None):
        if type(json_def) is str:
            json_def = json.loads(json_def)
        s = json_def
        self.pc_display = None if 'pc' not in s else self.pc_display_easy(s['pc'])
        self.pc_final = None if 'pc' not in s else self.pc_final_easy(s['pc'])
        self.mobile_display = None if 'mobile' not in s else self.mobile_display_easy(s['mobile'])
        self.mobile_final = None if 'mobile' not in s else self.mobile_final_easy(s['mobile'])
        self.headline = None if 'headline' not in s else s['headline']
        self.description = None if 'description' not in s else s['description']

    def pc_final_easy(self, pc):
        return pc['final']

    def pc_display_easy(self, pc):
        return pc['display']

    def mobile_final_easy(self, mobile):
        return mobile['final']

    def mobile_display_easy(self, mobile):
        return mobile['display']

class UpdateAdObject:
    def __init__(self, adAttr, nccAdId, inspectRequestMsg=None, userLock = None):
        self.adAttr = adAttr
        self.inspectRequestMsg = inspectRequestMsg
        self.nccAdId = nccAdId
        self.userLock = userLock

class CreateAdObject:
    def __init__(self, adObject, nccAdgroupId, type, inspectRequestMsg=None, userLock=None):
        self.ad = adObject
        self.inspectRequestMsg = inspectRequestMsg
        self.nccAdgroupId = nccAdgroupId
        self.type = type
        self.userLock = userLock

class AdObject:
    def __init__(self, json_def):
        if type(json_def) is str:
            json_def = json.loads(json_def)
        s = json_def
        self.ad = None if 'ad' not in s else AdFieldObject(s['ad'])
        self.adattr = None if 'adattr' not in s else s['adattr']
        self.customerId = None if 'customerId' not in s else s['customerId']
        self.editTm = None if 'editTm' not in s else s['editTm']
        self.inspectRequestMsg = None if 'inspectRequestMsg' not in s else s['inspectRequestMsg']
        self.inspectStatus = None if 'inspectStatus' not in s else s['inspectStatus']
        self.nccAdId = None if 'nccAdId' not in s else s['nccAdId']
        self.nccAdgroupId = None if 'nccAdgroupId' not in s else s['nccAdgroupId']
        self.regTm = None if 'regTm' not in s else s['regTm']
        self.status = None if 'status' not in s else s['status']
        self.statusReason = None if 'statusReason' not in s else s['statusReason']
        self.type = None if 'type' not in s else s['type']
        self.userLock = None if 'userLock' not in s else s['userLock']

class Ad:
    def __init__(self, base_url: str, api_key: str, secret_key: str, customer_id: int):
        self.conn = Connector(base_url, api_key, secret_key, customer_id)

    AdIdList = List[str]
    AdObjectList = List[AdObject]
    ChangeFieldsList = List[str]

    def get(self, adId: str, format=True) -> AdObject:
        result = self.conn.get('/ncc/ads/' + adId)
        if format in [False, 'json']:
            return result
        elif format in [True, 'object']:
            return AdObject(result)
        else:
            print(CommonFunctions.error_message('001'))

    def list_by_adgroup_id(self, nccAdGroupId: str, format=True) -> AdObjectList:
        result = self.conn.get('/ncc/ads', {'nccAdgroupId': nccAdGroupId})
        if format in [False, 'json']:
            return result
        elif format in [True, 'object', 'list']:
            adobj_list = []
            for arr in result:
                ad_obj = AdObject(arr)
                adobj_list.append(ad_obj)
            return adobj_list
        else:
            print(CommonFunctions.error_message('001'))

    def list(self, ids: AdIdList, format=True) -> AdObjectList:
        ids = ",".join(ids)
        ids = {'ids': ids}
        result = self.conn.get('/ncc/ads', ids)
        if format in [False, 'json']:
            return result
        elif format in [True, 'object', 'list']:
            ad_obj_list = []
            for arr in result:
                ad_obj = AdObject(arr)
                ad_obj_list.append(ad_obj)
            return ad_obj_list
        else:
            print(CommonFunctions.error_message('001'))

    def create(self, adObject, nccAdgroupId, type, inspectRequestMsg, userLock, format=True) -> AdObject:
        data = jsonpickle.encode(CreateAdObject(adObject, nccAdgroupId, type, inspectRequestMsg, userLock), unpicklable=False)
        data = json.loads(data)
        data = CommonFunctions.dropna(data)
        data_str = data
        data_str = json.dumps(data_str)
        result = self.conn.post('/ncc/ads', data_str)
        if format in [False, 'json']:
            return result
        elif format in [True, 'object', 'list']:
            return AdObject(result)
        else:
            print(CommonFunctions.error_message('001'))

    def update(self, adId: str, fields: ChangeFieldsList, adAttr, inspectRequestMsg, nccAdId, userLock, format=True) -> AdObject:
        change_fields_list = ",".join(fields)
        query = {'fields': change_fields_list}
        data = jsonpickle.encode(UpdateAdObject(adAttr=adAttr, inspectRequestMsg=inspectRequestMsg, nccAdId=nccAdId, userLock=userLock), unpicklable=False)
        data = json.loads(data)
        data = CommonFunctions.dropna(data)
        data_str = data
        data_str = json.dumps(data_str)
        result = self.conn.put('/ncc/ads/' + adId, data_str, query)
        if format in [False, 'json']:
            return result
        elif format in [True, 'object', 'list']:
            result = AdObject(result)
            return result
        else:
            print(CommonFunctions.error_message('001'))

    def delete(self, adId: str):
        self.conn.delete('/ncc/ads/' + adId)
        return True

    def copy(self, adId: str, targetAdGroupId: str, userLock: bool, format=True) -> AdObject:
        query = {'ids': adId, 'targetAdgroupId': targetAdGroupId, 'userLock': userLock}
        result = self.conn.put('/ncc/ads', None, query)
        if format in [False, 'json']:
            return result
        elif format in [True, 'object', 'list']:
            result = AdObject(result)
            return result
        else:
            print(CommonFunctions.error_message('001'))