from nevada.Common.Connector import *
from typing import List
import jsonpickle
import json

class CampaignAddObject:
    def __init__(self, customerId, campaignTp, name):
        self.customerId = customerId
        self.campaignTp = campaignTp
        self.dailyBudget = None
        self.deliveryMethod = None
        self.name = name
        self.periodEndDt = None
        self.periodStartDt = None
        self.trackingMode = None
        self.trackingUrl = None
        self.useDailyBudget = None
        self.usePeriod = None
        self.userLock = None

class CampaignUpdateObject:
    def __init__(self, lock, budget =None, period=None):
        if lock != None:
            self.userLock = bool(lock)
        if budget != None:
            self.useDailyBudget = bool(budget)
        if period != None:
            self.usePeriod = bool(period)

class CampaignObject():

    def __init__(self, json_def):
        if type(json_def) is str:
            json_def = json.loads(json_def)

        s = json_def

        self.campaignTp = None if 'campaignTp' not in s else s['campaignTp']
        self.customerId = None if 'customerId' not in s else s['customerId']
        self.dailyBudget = None if 'dailyBudget' not in s else s['dailyBudget']
        self.delFlag = None if 'delFlag' not in s else s['delFlag']
        self.deliveryMethod = None if 'deliveryMethod' not in s else s['deliveryMethod']
        self.editTm = None if 'editTm' not in s else s['editTm']
        self.expectCost = None if 'expectCost' not in s else s['expectCost']
        self.migType = None if 'migType' not in s else s['migType']
        self.name = None if 'name' not in s else s['name']
        self.nccCampaignId = None if 'nccCampaignId' not in s else s['nccCampaignId']
        self.periodEndDt = None if 'periodEndDt' not in s else s['periodEndDt']
        self.periodStartDt = None if 'periodStartDt' not in s else s['periodStartDt']
        self.regTm = None if 'regTm' not in s else s['regTm']
        self.status = None if 'status' not in s else s['status']
        self.statusReason = None if 'statusReason' not in s else s['statusReason']
        self.trackingMode = None if 'trackingMode' not in s else s['trackingMode']
        self.trackingUrl = None if 'trackingUrl' not in s else s['trackingUrl']
        self.useDailyBudget = None if 'useDailyBudget' not in s else s['useDailyBudget']
        self.usePeriod = None if 'usePeriod' not in s else s['usePeriod']
        self.userLock = None if 'userLock' not in s else s['userLock']


class Campaign:
    def __init__(self, base_url: str, api_key: str, secret_key: str, customer_id: int):
        self.conn = Connector(base_url, api_key, secret_key, customer_id)

    CampaignList = List[CampaignObject]
    CampaignIdList = List[str]
    ChangeFieldsList = List[str]

    def get_campaign_list(self, campaignType: str = None, baseSearchId: str = None, recordSize: int = None,
                          selector: str = None) -> CampaignList:

        query = {'campaignType': campaignType, 'baseSearchId': baseSearchId, 'recordSize': recordSize,
                 'selector': selector}
        result = self.conn.get('/ncc/campaigns', query)

        camp_list = []
        for arr in result:
            camp = CampaignObject(arr)
            camp_list.append(camp)
        return camp_list

    def get_campaign_list_by_ids(self, ids: CampaignIdList) -> CampaignList:
        ids = ",".join(ids)
        query = {'ids': ids}

        result = self.conn.get('/ncc/campaigns', query)

        camp_list = []
        for arr in result:
            camp = CampaignObject(arr)
            camp_list.append(camp)
        return camp_list

    def get_campaign(self, campaignId: str) -> CampaignObject:
        result = self.conn.get('/ncc/campaigns/' + campaignId)
        camp = CampaignObject(result)
        return camp

    def create_campaign(self, campaign_add_object: CampaignAddObject):

        data = jsonpickle.encode(campaign_add_object, unpicklable=False)
        data = json.loads(data)
        data = CommonFunctions.dropna(data)
        data_str = json.dumps(data)
        result = self.conn.post('/ncc/campaigns', data_str)
        camp = CampaignObject(result)
        return camp

    def update_campaign(self, campaign_update_object: CampaignUpdateObject, campaignId: str,
                        fields: ChangeFieldsList) -> CampaignList:
        fields = ",".join(fields)
        fields = {'fields': fields}
        data = jsonpickle.encode(campaign_update_object, unpicklable=False)
        result = self.conn.put('/ncc/campaigns/' + str(campaignId), data, fields)  # userLock, budget, period
        camp = CampaignObject(result)
        return camp
