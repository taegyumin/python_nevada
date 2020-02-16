from nevada.Common.Connector import *
from typing import List
import json

class StatDataObject:
    def __init__(self, json_def):
        if type(json_def) is str:
            json_def = json.loads(json_def)
        s = json_def
        self.avgRnk = None if 'avgRnk' not in s else s['avgRnk']
        self.ccnt = None if 'ccnt' not in s else s['ccnt']
        self.clkCnt = None if 'clkCnt' not in s else s['clkCnt']
        self.cpc = None if 'cpc' not in s else s['cpc']
        self.ctr = None if 'ctr' not in s else s['ctr']
        self.dateEnd = None if 'dateEnd' not in s else s['dateEnd']
        self.dateStart = None if 'dateStart' not in s else s['dateStart']
        self.drtCrto = None if 'drtCrto' not in s else s['drtCrto']
        self.impCnt = None if 'impCnt' not in s else s['impCnt']
        self.salesAmt = None if 'salesAmt' not in s else s['salesAmt']

class SummaryObject:
    def __init__(self, json_def):
        if type(json_def) is str:
            json_def = json.loads(json_def)
        s = json_def
        self.dateEnd = None if 'dateEnd' not in s else s['dateEnd']
        self.dateStart = None if 'dateStart' not in s else s['dateStart']

class StatTypeObject:
    def __init__(self, json_def):
        if type(json_def) is str:
            json_def = json.loads(json_def)
        s = json_def
        self.clkCnt = None if 'clkCnt' not in s else s['clkCnt']
        self.drtCrto = None if 'drtCrto' not in s else s['drtCrto']
        self.salesAmt = None if 'salesAmt' not in s else s['salesAmt']
        self.schKeyword = None if 'schKeyword' not in s else s['schKeyword']

class StatObject:
    def __init__(self, json_def):
        if type(json_def) is str:
            json_def = json.loads(json_def)
        s = json_def
        self.data = None if 'data' not in s else self.match_data(s['data'])  # list
        self.summary = None if 'data' not in s else SummaryObject(s['data'])

    def match_data(self, s):
        stat_list = []
        for arr in s:
            stat = StatDataObject(arr)
            stat_list.append(stat)
        return stat_list

class Stat:
    def __init__(self, base_url: str, api_key: str, secret_key: str, customer_id: int):
        self.conn = Connector(base_url, api_key, secret_key, customer_id)

    StatIdList = List[str]

    def get_stat_by_id(self, id: str, fields: str, timeRange: str, dataPreset: str = None, timeIncrement: str = None,
                       breakdown: str = None) -> StatObject:
        query = {'id': id, 'fields': fields, 'timeRange': timeRange, 'dataPreset': dataPreset,
                 'timeIncrement': timeIncrement, 'breakdown': breakdown}
        result = self.conn.get('/stats', query)
        result = StatObject(result)
        return result

    def get_stat_by_ids(self, ids: StatIdList, fields: str, timeRange: str, dataPreset: str = None,
                        timeIncrement: str = None, breakdown: str = None) -> StatObject:
        query = {'ids': ids, 'fields': fields, 'timeRange': timeRange, 'dataPreset': dataPreset,
                 'timeIncrement': timeIncrement, 'breakdown': breakdown}
        result = self.conn.get('/stats', query)
        result = StatObject(result)
        return result

    def get_stat_by_type(self, id: str, statType: str) -> StatTypeObject:
        query = {'id': id, 'statType': statType}
        result = self.conn.get('/stats', query)
        result = StatTypeObject(result)
        return result
