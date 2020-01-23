from nevada.Common.Connector import *
from typing import List
import jsonpickle
import json


# pylint: disable=C0103
# pylint: disable=E0401

class targetSummaryObject:
    def __init__(self, json_def):
        if type(json_def) is str:
            json_def = json.loads(json_def)
        s = json_def
        self.media = None if 'media' not in s else s['media']
        self.pcMobile = None if 'pcMobile' not in s else s['pcMobile']
        self.region = None if 'region' not in s else s['region']
        self.time = None if 'time' not in s else s['time']
        self.week = None if 'week' not in s else s['week']

class target:
    def __init__(self, json_def):
        if type(json_def) is str:
            json_def = json.loads(json_def)
        s = json_def
        self.delFlag = None if 'delFlag' not in s else s['delFlag']
        self.editTm = None if 'editTm' not in s else s['editTm']
        self.nccTargetId = None if 'nccTargetId' not in s else s['nccTargetId']
        self.ownerId = None if 'ownerId' not in s else s['ownerId']
        self.regTm = None if 'regTm' not in s else s['regTm']
        self.target = None if 'target' not in s else s['target']
        self.targetTp = None if 'targetTp' not in s else s['targetTp']

class adgroupAttrObject:
    def __init__(self, json_def=None):
        if type(json_def) is str:
            json_def = json.loads(json_def)
        s = json_def
        self.campaignTp = None if 'campaignTp' not in s else s['campaignTp']

class RestrictedKeyword:
    def __init__(self, json_def):
        if type(json_def) is str:
            json_def = json.loads(json_def)
        s = json_def
        self.delFlag = None if 'delFlag' not in s else s['delFlag']
        self.keyword = None if 'keyword' not in s else s['keyword']
        self.nccAdgroupId = None if 'nccAdgroupId' not in s else s['nccAdgroupId']
        self.nccAdgroupRestrictKwdId = None if 'nccAdgroupRestrictKwdId' not in s else s['nccAdgroupRestrictKwdId']
        self.regTm = None if 'regTm' not in s else s['regTm']
        self.type = None if 'type' not in s else s['type']

class UpdateEntireAdgroupObject:
    def __init__(self, bidAmt, contentsNetworkBidAmt, dailyBudget, keywordPlusWeight, mobileNetworkBidWeight, nccAdgroupId,
                    pcNetworkBidWeight, useCntsNetworkBidAmt, useDailyBudget, useKeywordPlus, userLock):
     self.bidAmt = bidAmt
     self.budgetLock = None
     self.contentsNetworkBidAmt = contentsNetworkBidAmt
     self.dailyBudget = dailyBudget
     self.keywordPlusWeight = keywordPlusWeight
     self.mobileChannelId = None
     self.mobileNetworkBidWeight = mobileNetworkBidWeight
     self.name = None
     self.nccAdgroupId = nccAdgroupId
     self.nccCampaignId = None
     self.pcNetworkBidWeight = pcNetworkBidWeight
     #self.targts = None
     self.useCntsNetworkBidAmt = useCntsNetworkBidAmt
     self.useDailyBudget = useDailyBudget
     self.useKeywordPlus = useKeywordPlus
     self.userLock = userLock


class UpdateAdgroupObject:
    def __init__(self, bidAmt=None, userLock=None, useKeywordPlus=None, networkBidWeight=None,
                 targetLocation=None, targetTime=None, targetMedia=None):
        self.bidAmt = bidAmt
        self.userLock = userLock
        self.useKeywordPlus = useKeywordPlus
        self.useCntsNetworkBidAmt = networkBidWeight
        # self.target = self.make_target_obj(targetLocation, targetTime, targetLocation)
        self.targetLoaction = targetLocation
        self.targetTime = targetTime
        self.targetMedia = targetMedia

    def make_target_obj(self, nccTargetId, ownerId, targetLocation, targetTime, targetLoaction):
        target_obj = []
        if targetLoaction != None:
            target_obj.append(targetLoaction)
        if targetTime != None:
            target_obj.append(targetTime)
        if targetLoaction != None:
            targetLoaction.append(targetLoaction)
        return targetLoaction

class RestrictedKeywordsObject:
    def __init__(self, keyword, description, nccAdgroupId):
        self.delFlag = False
        self.description = description
        self.keyword = keyword
        self.nccAdgroupId = nccAdgroupId
        self.type = "KEYWORD_PLUS_RESTRICT"


class CreateAdgroupObject:
    def __init__(self, ncc_campaign_id, name, pc_channel_id, mobile_channel_id):
        self.adgroupAttrJson = {'contentsType' : 'PRODUCT'}
        self.bidAmt = None
        self.budgetLock = None
        self.contentsNetworkBidAmt = None
        self.dailyBudget = None
        self.keywordPlusWeight = None
        self.mobileChannelId = mobile_channel_id
        self.mobileNetworkBidWeight = None
        self.name = name
        self.nccCampaignId = ncc_campaign_id
        self.pcChannelId = pc_channel_id
        self.pcNetworkBidWeight = None
        self.targets = None #target object
        self.useCntsNetworkBidAmt = None
        self.useDailyBudget = None
        self.useKeywordPlus = None
        self.userLock = None


class AdgroupObject:
    def __init__(self, json_def):
        if type(json_def) is str:
            json_def = json.loads(json_def)
        s = json_def
        self.adgroupAttrJson = None if 'adgroupAttrJson' not in s else self.__match_group_attr(s['adgroupAttrJson'])
        self.bidAmt = None if 'bidAmt' not in s else s['bidAmt']
        self.budgetLock = None if 'budgetLock' not in s else s['budgetLock']
        self.contentsNetworkBidAmt = None if 'contentsNetworkBidAmt' not in s else s['contentsNetworkBidAmt']
        self.customerId = None if 'customerId' not in s else s['customerId']
        self.dailyBudget = None if 'dailyBudget' not in s else s['dailyBudget']
        self.delFlag = None if 'delFlag' not in s else s['delFlag']
        self.editTm = None if 'editTm' not in s else s['editTm']
        self.expectCost = None if 'expectCost' not in s else s['expectCost']
        self.keywordPlusWeight = None if 'keywordPlusWeight' not in s else s['keywordPlusWeight']
        self.migType = None if 'migType' not in s else s['migType']
        self.mobileChannelId = None if 'mobileChannelId' not in s else s['mobileChannelId']
        self.mobileChannelKey = None if 'mobileChannelKey' not in s else s['mobileChannelKey']
        self.mobileNetworkBidWeight = None if 'mobileNetworkBidWeight' not in s else s['mobileNetworkBidWeight']
        self.name = None if 'name' not in s else s['name']
        self.nccAdgroupId = None if 'nccAdgroupId' not in s else s['nccAdgroupId']
        self.nccCampaignId = None if 'nccCampaignId' not in s else s['nccCampaignId']
        self.pcChannelId = None if 'pcChannelId' not in s else s['pcChannelId']
        self.pcChannelKey = None if 'pcChannelKey' not in s else s['pcChannelKey']
        self.pcNetworkBidWeight = None if 'pcNetworkBidWeight' not in s else s['pcNetworkBidWeight']
        self.regTm = None if 'regTm' not in s else s['regTm']
        self.status = None if 'status' not in s else s['status']
        self.statusReason = None if 'statusReason' not in s else s['statusReason']
        self.targets = None if 'targets' not in s else self.__match_target(s['targets'])
        self.targetSummary = None if 'targetSummary' not in s else self.__match_target_summary(s['targetSummary'])
        self.useCntsNetworkBidAmt = None if 'useCntsNetworkBidAmt' not in s else s['useCntsNetworkBidAmt']
        self.useDailyBudget = None if 'useDailyBudget' not in s else s['useDailyBudget']
        self.useKeywordPlus = None if 'useKeywordPlus' not in s else s['useKeywordPlus']
        self.userLock = None if 'userLock' not in s else s['userLock']

    def __match_target(self, sarray):
        target_list = []
        for arr in sarray:
            target_item = target(arr)
            target_list.append(target_item)

        return target_list

    def __match_target_summary(self, sarray):
       summary = targetSummaryObject(sarray)
       return summary

    def __match_group_attr(self, sarray):
        attr = adgroupAttrObject(sarray)
        return attr

class Adgroup:
    def __init__(self, base_url: str, api_key: str, secret_key: str, customer_id: int):
        self.conn = Connector(base_url, api_key, secret_key, customer_id)

    RestrictedKeywordsAddObject = List[RestrictedKeywordsObject]
    RestrictedKeywordList = List[RestrictedKeyword]
    AdgroupList = List[AdgroupObject]
    AdgroupIdList = List[str]
    RestrictedKeywordIdList = List[str]
    ChangeFieldsList = List[str]

    def get_restricted_keyword(self, adgroupId: str) -> RestrictedKeywordList:
        query = {'type': 'KEYWORD_PLUS_RESTRICT'}
        result = self.conn.get('/ncc/adgroups/' + adgroupId + "/restricted-keywords", query);
        restricted_list = []
        for arr in result:
            restricted_keyword = RestrictedKeyword(arr)
            restricted_list.append(restricted_keyword)
        return restricted_list

    def get_adgroup_list(self, nccCampaignId: str = None, baseSearchId: str = None,
                         recordSize: int = None, selector: str = None) -> AdgroupList:

        query = {'nccCampaignId': nccCampaignId, 'baseSearchId': baseSearchId,
                 'record_size': recordSize, 'selector': selector}
        result = self.conn.get('/ncc/adgroups', query)
        adgroup_list = []
        for arr in result:
            camp = AdgroupObject(arr)
            adgroup_list.append(camp)
        return adgroup_list

    def get_adgroup_list_by_ids(self, ids: AdgroupIdList) -> AdgroupList:
        ids = ",".join(ids)
        query = {'ids': ids}
        result = self.conn.get('/ncc/adgroups', query)
        adgroup_list = []
        for arr in result:
            camp = AdgroupObject(arr)
            adgroup_list.append(camp)
        return adgroup_list

    def get_adgroup_by_adgroupid(self, adgroupId: str) -> AdgroupObject:
        result = self.conn.get('/ncc/adgroups/' + adgroupId)
        adgroup = AdgroupObject(result)
        return adgroup

    def create_restricted_keyword(self, adgroupId: str,
                                  restricted_keywords_object: RestrictedKeywordsAddObject) -> RestrictedKeyword:
        data = jsonpickle.encode(restricted_keywords_object, unpicklable=False)
        data = json.loads(data)
        data = CommonFunctions.dropna(data)
        data_str = [data]
        data_str = json.dumps(data_str);
        result = self.conn.post('/ncc/adgroups/%s/restricted-keywords' % str(adgroupId), data_str)
        restrict_keyword = RestrictedKeyword(result)

        return restrict_keyword

    def create_adgroup(self, create_adgroup_object: CreateAdgroupObject):
        data = jsonpickle.encode(create_adgroup_object, unpicklable=False)
        data = json.loads(data)
        data = CommonFunctions.dropna(data)
        data_str = json.dumps(data)
        result = self.conn.post('/ncc/adgroups', data_str)
        result = AdgroupObject(result)
        return result

    def update_adgroup(self, adgroupId: str, fields: ChangeFieldsList, UpdateAdgroupObject: UpdateAdgroupObject):
        change_fields_list = ",".join(fields)
        query = {'fields': change_fields_list}
        data = jsonpickle.encode(UpdateAdgroupObject, unpicklable=False)
        data = json.loads(data)
        data = CommonFunctions.dropna(data)
        data_str = json.dumps(data)
        result = self.conn.put('/ncc/adgroups/' + adgroupId, data_str, query)
        result = AdgroupObject(result)
        return result

    def update_adgroup_entire(self, adgroupId: str, UpdateEntireAdgroupObject: UpdateEntireAdgroupObject):
        data = jsonpickle.encode(UpdateEntireAdgroupObject, unpicklable=False)
        data = json.loads(data)
        data = CommonFunctions.dropna(data)
        data_str = json.dumps(data)
        result = self.conn.put('/ncc/adgroups/' + adgroupId, data_str)
        result = AdgroupObject(result)
        return result

    def delete_group_restricted_keyword(self, adgroupId: str, res_keyword_ids: RestrictedKeywordIdList):
        res_keyword_ids = ",".join(res_keyword_ids)
        query = {'ids': res_keyword_ids}
        result = self.conn.delete('/ncc/adgroups/%s/restricted-keywords' % str(adgroupId), query)
        return True

    def delete_adgroup(self, adgroupId: str):
        result = self.conn.delete('/ncc/adgroups/' + adgroupId)
        return True
