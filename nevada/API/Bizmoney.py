from nevada.Common.Connector import *
from typing import List
import json

class BizmoneyObject:
    def __init__(self, json_def):
        if type(json_def) is str:
            json_def = json.loads(json_def)
        s = json_def
        self.bizmoney = None if 'bizmoney' not in s else s['bizmoney']
        self.budgetLock = None if 'budgetLock' not in s else s['budgetLock']
        self.customerId = None if 'customerId' not in s else s['customerId']
        self.refundLock = None if 'refundLock' not in s else s['refundLock']

class BizmoneyCostObject:
    def __init__(self, json_def):
        if type(json_def) is str:
            json_def = json.loads(json_def)
        s = json_def
        self.adjustedNonRefundableAmt = None if 'adjustedNonRefundableAmt' not in s else s['adjustedNonRefundableAmt']
        self.adjustedRefundableAmt = None if 'adjustedRefundableAmt' not in s else s['adjustedRefundableAmt']
        self.customerId = None if 'customerId' not in s else s['customerId']
        self.date = None if 'date' not in s else s['date']
        self.device = None if 'device' not in s else s['device']
        self.networkType = None if 'networkType' not in s else s['networkType']
        self.nonRefundableAmt = None if 'nonRefundableAmt' not in s else s['nonRefundableAmt']
        self.productCode = None if 'productCode' not in s else s['productCode']
        self.refundableAmt = None if 'refundableAmt' not in s else s['refundableAmt']

class BizmoneyChargeObject:
    def __init__(self, json_def):
        if type(json_def) is str:
            json_def = json.loads(json_def)
        s = json_def
        self.displayCd = None if 'displayCd' not in s else s['displayCd']
        self.displayName = None if 'displayName' not in s else s['displayName']
        self.newNonRefundableAmt = None if 'newNonRefundableAmt' not in s else s['newNonRefundableAmt']
        self.newRefundableAmt = None if 'newRefundableAmt' not in s else s['newRefundableAmt']
        self.statDt = None if 'statDt' not in s else s['statDt']

class BizmoneyExhaustObject:
    def __init__(self, json_def):
        if type(json_def) is str:
            json_def = json.loads(json_def)
        s = json_def
        self.activityCd = None if 'activityCd' not in s else s['activityCd']
        self.campaignTp = None if 'campaignTp' not in s else s['campaignTp']
        self.customerId = None if 'customerId' not in s else s['customerId']
        self.prodInfoCd = None if 'prodInfoCd' not in s else s['prodInfoCd']
        self.settleDt = None if 'settleDt' not in s else s['settleDt']
        self.useNonrefundableAmt = None if 'useNonrefundableAmt' not in s else s['useNonrefundableAmt']
        self.useRefundableAmt = None if 'useRefundableAmt' not in s else s['useRefundableAmt']

class BizmoneyPeriodObject:
    def __init__(self, json_def):
        if type(json_def) is str:
            json_def = json.loads(json_def)
        s = json_def
        self.addNonRefundableAmt = None if 'addNonRefundableAmt' not in s else s['addNonRefundableAmt']
        self.addRefundableAmt = None if 'addRefundableAmt' not in s else s['addRefundableAmt']
        self.customerId = None if 'customerId' not in s else s['customerId']
        self.nonRefundableAmt = None if 'nonRefundableAmt' not in s else s['nonRefundableAmt']
        self.refundNonRefundableAmt = None if 'refundNonRefundableAmt' not in s else s['refundNonRefundableAmt']
        self.refundRefundableAmt = None if 'refundRefundableAmt' not in s else s['refundRefundableAmt']
        self.refundableAmt = None if 'refundableAmt' not in s else s['refundableAmt']
        self.returnRefundableAmt = None if 'returnRefundableAmt' not in s else s['returnRefundableAmt']
        self.settleDt = None if 'settleDt' not in s else s['settleDt']
        self.useNonRefundableAmt = None if 'useNonRefundableAmt' not in s else s['useNonRefundableAmt']
        self.useRefundableAmt = None if 'useRefundableAmt' not in s else s['useRefundableAmt']

class Bizmoney:
    def __init__(self, base_url: str, api_key: str, secret_key: str, customer_id: int):
        self.conn = Connector(base_url, api_key, secret_key, customer_id)

    BizmoneyCostObjectList = List[BizmoneyCostObject]
    BizmoneyChargeObjectList = List[BizmoneyChargeObject]
    BizmoneyExhaustObjectList = List[BizmoneyExhaustObject]
    BizmoneyPeriodObjectList = List[BizmoneyPeriodObject]

    def get_biz_money(self, format=True) -> BizmoneyObject:
        result = self.conn.get('/billing/bizmoney')
        if format in [False, 'json']:
            return result
        elif format in [True, 'object', 'list']:
            return BizmoneyObject(result)
        else:
            print('Please Check the input value of format.')

    def get_cost(self, statDt: str, searchStartDt:str, searchEndDt:str, format=True) -> BizmoneyCostObjectList:
        ## 채워야 함
        result = self.conn.get('/billing/bizmoney/cost/' + statDt)
        if format in [False, 'json']:
            return result
        elif format in [True, 'object', 'list']:
            cost_list = []
            for arr in result:
                cost = BizmoneyCostObject(arr)
                cost_list.append(cost)
            return cost_list
        else:
            print('Please Check the input value of format.')

    def get_charge(self, searchStartDt:str, searchEndDt:str, format=True) -> BizmoneyChargeObjectList:
        ## 채워야 함
        result = self.conn.get('/billing/bizmoney/histories/charge{?searchStartDt,searchEndDt}')
        if format in [False, 'json']:
            return result
        elif format in [True, 'object', 'list']:
            charge_list = []
            for arr in result:
                charge = BizmoneyChargeObject(arr)
                charge_list.append(charge)
            return charge_list
        else:
            print('Please Check the input value of format.')

    def get_exhaust(self, searchStartDt:str, searchEndDt:str, format=True) -> BizmoneyExhaustObjectList:
        ## 채워야 함
        result = self.conn.get('/billing/bizmoney/histories/exhaust{?searchStartDt,searchEndDt}')
        if format in [False, 'json']:
            return result
        elif format in [True, 'object', 'list']:
            exhaust_list = []
            for arr in result:
                exhaust = BizmoneyExhaustObject(arr)
                exhaust_list.append(exhaust)
            return exhaust_list
        else:
            print('Please Check the input value of format.')


    def get_period(self, searchStartDt:str, searchEndDt:str, format=True) -> BizmoneyPeriodObjectList:
        result = self.conn.get('/billing/bizmoney/histories/period{?searchStartDt,searchEndDt}')
        if format in [False, 'json']:
            return result
        elif format in [True, 'object', 'list']:
            period_list = []
            for arr in result:
                period = BizmoneyPeriodObject(arr)
                period_list.append(period)
            return period_list
        else:
            print('Please Check the input value of format.')


