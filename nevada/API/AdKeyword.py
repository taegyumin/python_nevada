from nevada.Common.Connector import *
from typing import List
import jsonpickle
import json

class CreateAdKeywordObject:
    def __init__(self, keyword):
        self.bidAmt = None
        self.customerId = None
        self.keyword = keyword
        self.useGroupBidAmt = None
        self.userLock = None

class UpdateAdKeywordObject:
    def __init__(self, nccAdgroupId, nccKeywordId):
        self.bidAmt = None
        self.links = None
        self.nccAdgroupId = nccAdgroupId
        self.nccKeywordId = nccKeywordId
        self.useGroupBidAmt = None
        self.userLock = None

class ManagedKeywordInfoObject:
    def __init__(self, json_def):
        if type(json_def) is str:
            json_def = json.loads(json_def)
        s = json_def
        self.PCPLMaxDepth = None if 'PCPLMaxDepth' not in s else s['PCPLMaxDepth']
        self.editTm = None if 'editTm' not in s else s['editTm']
        self.isAdult = None if 'isAdult' not in s else s['isAdult']
        self.isBrand = None if 'isBrand' not in s else s['isBrand']
        self.isLowSearchVolume = None if 'isLowSearchVolume' not in s else s['isLowSearchVolume']
        self.isRestricted = None if 'isRestricted' not in s else s['isRestricted']
        self.isSeason = None if 'isSeason' not in s else s['isSeason']
        self.isSellProhibit = None if 'isSellProhibit' not in s else s['isSellProhibit']
        self.keyword = None if 'keyword' not in s else s['keyword']
        self.regTm = None if 'regTm' not in s else s['regTm']

class ManagedKeywordObject:
    def __init__(self, json_def):
        if type(json_def) is str:
            json_def = json.loads(json_def)
        s = json_def
        self.keyword = None if 'keyword' not in s else s['keyword']
        self.managedKeyword = None if 'managedKeyword' not in s else ManagedKeywordInfoObject(s['managedKeyword'])

class AdKeywordObject:
    def __init__(self, json_def):
        if type(json_def) is str:
            json_def = json.loads(json_def)
        s = json_def
        self.bidAmt = None if 'bidAmt' not in s else s['bidAmt']
        self.customerId = None if 'customerId' not in s else s['customerId']
        self.editTm = None if 'editTm' not in s else s['editTm']
        self.inspectStatus = None if 'inspectStatus' not in s else s['inspectStatus']
        self.keyword = None if 'keyword' not in s else s['keyword']
        self.nccAdgroupId = None if 'nccAdgroupId' not in s else s['nccAdgroupId']
        self.nccCampaignId = None if 'nccCampaignId' not in s else s['nccCampaignId']
        self.nccKeywordId = None if 'nccKeywordId' not in s else s['nccKeywordId']
        self.nccQi = None if 'nccQi' not in s else s['nccQi']
        self.regTm = None if 'regTm' not in s else s['regTm']
        self.status = None if 'status' not in s else s['status']
        self.statusReason = None if 'statusReason' not in s else s['statusReason']
        self.useGroupBidAmt = None if 'useGroupBidAmt' not in s else s['useGroupBidAmt']
        self.userLock = None if 'userLock' not in s else s['userLock']


class AdKeyword:
    def __init__(self, base_url: str, api_key: str, secret_key: str, customer_id: int):
        self.conn = Connector(base_url, api_key, secret_key, customer_id)

    AdKeywordList = List[AdKeywordObject]
    AdKeywordIdList = List[str]
    KeywordsList = List[str]

    def get_adkeyword_list_by_label_id(self, nccLabelId: str) -> AdKeywordList:
        query = {'nccLabelId': nccLabelId}
        result = self.conn.get('/ncc/keywords', query)

        adkeyword_list = []
        for arr in result:
            keyword = AdKeywordObject(arr)
            adkeyword_list.append(keyword)

        return adkeyword_list

    def get_adkeyword_list_by_ids(self, ids: AdKeywordIdList) -> AdKeywordList:
        ids = ",".join(ids)
        query = {'ids': ids}
        result = self.conn.get('/ncc/keywords', query)

        adkeyword_list = []
        for arr in result:
            keyword = AdKeywordObject(arr)
            adkeyword_list.append(keyword)

        return adkeyword_list

    def get_adkeyword_list_by_group_id(self, nccAdgroupId: str = None, baseSearchId: str = None,
                                       recordSize: int = None, selector: str = None) -> AdKeywordList:

        query = {'nccAdgroupId': nccAdgroupId, 'baseSearchId': baseSearchId, 'recordSize': recordSize,
                 'selector': selector}
        result = self.conn.get('/ncc/keywords', query)

        adkeyword_list = []
        for arr in result:
            keyword = AdKeywordObject(arr)
            adkeyword_list.append(keyword)

        return adkeyword_list

    def get_adkeyword(self, nccKeywordId) -> AdKeywordObject:
        result = self.conn.get('/ncc/keywords/' + nccKeywordId)
        result = AdKeywordObject(result)
        return result

    def create_adkeyword(self, nccAdgroupId, CreateAdKeywordObject) -> AdKeywordObject:
        data = jsonpickle.encode(CreateAdKeywordObject, unpicklable=False)
        data = json.loads(data)
        data = CommonFunctions.dropna(data)
        data = [data]
        data_str = json.dumps(data)

        result = self.conn.post('/ncc/keywords', data_str, {'nccAdgroupId': nccAdgroupId})
        result = AdKeywordObject(result)
        return result

    def update_adkeyrword(self, nccKeywordId, fields, UpdateAdKeywordObject) -> AdKeywordObject:
        data = jsonpickle.encode(UpdateAdKeywordObject, unpicklable=False)
        data = json.loads(data)
        data = CommonFunctions.dropna(data)
        data_str = json.dumps(data)

        query = {'fields': fields}

        result = self.conn.put('/ncc/keywords/' + nccKeywordId, data_str, query)
        result = AdKeywordObject(result)
        return result

    def delete_adkeyword(self, nccKeywordId: str):
        self.conn.delete('/ncc/keywords/' + nccKeywordId)
        return True

    def delete_adkeyword_many(self, ids: AdKeywordIdList):
        ids = ",".join(ids)
        query = {'ids': ids}
        self.conn.delete('/ncc/keywords', query)

    def managed_keyword_list(self, keywords: KeywordsList) -> ManagedKeywordObject:
        keywords = ",".join(keywords)
        query = {'keywords': keywords}
        result = self.conn.get('/ncc/managedKeyword', query)

        managedkeyword_list = []
        for arr in result:
            managedkeyword = ManagedKeywordObject(arr)
            managedkeyword_list.append(managedkeyword)
        return managedkeyword_list
