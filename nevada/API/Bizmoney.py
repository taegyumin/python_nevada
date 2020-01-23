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

class Bizmoney:
    def __init__(self, base_url: str, api_key: str, secret_key: str, customer_id: int):
        self.conn = Connector(base_url, api_key, secret_key, customer_id)

    BizmoneyCostObjectList = List[BizmoneyCostObject]

    def get_biz_money_json(self):
        result = self.conn.get('/billing/bizmoney')
        return result

    def get_biz_money_list(self) -> BizmoneyObject:
        result_json = self.get_biz_money_json()
        result = BizmoneyObject(result_json)
        return result

    def get_biz_money_cost_json(self, statDt: str):
        result = self.conn.get('/billing/bizmoney/cost/' + statDt)
        return result

    def get_biz_money_cost_list(self, statDt: str) -> BizmoneyCostObjectList:
        result_json = self.get_biz_money_cost_json(statDt)
        cost_list = []
        for arr in result_json:
            cost = BizmoneyCostObject(arr)
            cost_list.append(cost)
        return cost_list
