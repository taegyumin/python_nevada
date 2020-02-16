from nevada.Common.Connector import *
from typing import List
import jsonpickle
import json

class KeyAndPositionObject:
    def __init__(self, key, position):
        self.key = key
        self.position = position

class GetAvgPositionBidObject:
    def __init__(self, device, KeyAndPositonObject):
        self.device = device
        self.items = KeyAndPositonObject

class GetExposureMiniBidObject:
    def __init__(self, device, period, keys):
        self.device = device
        self.period = period
        self.items = keys

class GetMedianBidObject:
    def __init__(self, device, period, keys):
        self.device = device
        self.period = period
        self.items = keys

class GetPerformanceObject:
    def __init__(self, device, keywordplus, key, bids):
        self.device = device
        self.keywordplus = keywordplus
        self.key = key
        self.bids = bids

class GetPerformanceBulkObject:
    def __init__(self, device, keywordplus, keyword, bid):
        self.device = device
        self.keywordplus = keywordplus
        self.keyword = keyword
        self.bid = bid

class EstimateAvgObject:
    def __init__(self, json_def):
        if type(json_def) is str:
            json_def = json.loads(json_def)
        s = json_def
        self.bid = None if 'bid' not in s else s['bid']
        self.keyword = None if 'keyword' not in s else s['keyword']
        #self.nccKeywordId = None if 'nccKeywordId' not in s else s['nccKeywordId']
        self.position = None if 'position' not in s else s['position']

class EstimateExposureMiniObject:
    def __init__(self, json_def):
        if type(json_def) is str:
            json_def = json.loads(json_def)
        s = json_def
        self.bid = None if 'bid' not in s else s['bid']
        self.keyword = None if 'keyword' not in s else s['keyword']

class EstimateMedianObject:
    def __init__(self, json_def):
        if type(json_def) is str:
            json_def = json.loads(json_def)
        s = json_def
        self.bid = None if 'bid' not in s else s['bid']
        self.keyword = None if 'keyword' not in s else s['keyword']

class EstimatePerformanceObject:
    def __init__(self, json_def):
        if type(json_def) is str:
            json_def = json.loads(json_def)
        s = json_def
        self.bid = None if 'bid' not in s else s['bid']
        self.clicks = None if 'clicks' not in s else s['clicks']
        self.cost = None if 'cost' not in s else s['cost']
        self.impressions = None if 'impressions' not in s else s['impressions']
        self.cost_per_click = int(self.cost / self.clicks)

class EstimatePerformanceBulkObject:
    def __init__(self, device, keywordplus, keyword, bid, clicks, impressions, cost):
        self.device = device
        self.keywordplus = keywordplus
        self.keyword = keyword
        self.bid = bid
        self.clicks = clicks
        self.impressions = impressions
        self.cost = cost
        self.cost_per_click = int(self.cost / self.clicks)

class Estimate:
    def __init__(self, base_url: str, api_key: str, secret_key: str, customer_id: int):
        self.conn = Connector(base_url, api_key, secret_key, customer_id)

    EstimateAvgObjectList = List[EstimateAvgObject]
    EstimateMedianObjectList = List[EstimateMedianObject]
    EstimateExposureMiniObjectList = List[EstimateExposureMiniObject]
    EstimatePerformanceObjectList = List[EstimatePerformanceObject]
    GetPerformanceObjectList = List[GetPerformanceObject]
    GetPerformanceBulkObjectList = List[GetPerformanceBulkObject]

    def get_avg_position_bid_json(self, type, device, key_and_position_list):
        temp = []
        for key_and_position in key_and_position_list:
             temp.append(KeyAndPositionObject(key_and_position[0],key_and_position[1]))
        data = jsonpickle.encode(GetAvgPositionBidObject(device, temp), unpicklable=False)
        data = json.loads(data)
        data = CommonFunctions.dropna(data)
        data_str = json.dumps(data)
        result = self.conn.post('/estimate/average-position-bid/' + type, data_str)
        result = result['estimate']
        return result

    def get_avg_position_bid_list(self, type, device, key_and_position_list) -> EstimateAvgObjectList:
        result_json = self.get_avg_position_bid_json(type, device, key_and_position_list)
        estimate_list = []
        for arr in result_json:
            estimate = EstimateAvgObject(arr)
            estimate_list.append(estimate)
        return estimate_list

    def get_exposure_mini_bid_json(self, type: str, device, period, keys):
        data = jsonpickle.encode(GetExposureMiniBidObject(device, period, keys), unpicklable=False)
        data = json.loads(data)
        data = CommonFunctions.dropna(data)
        data_str = json.dumps(data)
        result = self.conn.post('/estimate/exposure-minimum-bid/' + type, data_str)
        result = result['estimate']
        return result

    def get_exposure_mini_bid_list(self, type: str, device, period, keys) -> EstimateExposureMiniObjectList:
        result_json = self.get_exposure_mini_bid_json(type, device, period, keys)
        estimate_list = []
        for arr in result_json:
            estimate = EstimateExposureMiniObject(arr)
            estimate_list.append(estimate)
        return estimate_list

    def get_median_bid_json(self, type: str, device, period, keys):
        data = jsonpickle.encode(GetMedianBidObject(device, period, keys), unpicklable=False)
        data = json.loads(data)
        data = CommonFunctions.dropna(data)
        data_str = json.dumps(data)
        result = self.conn.post('/estimate/median-bid/' + type, data_str)
        result = result['estimate']
        return result

    def get_median_bid_list(self, type: str, device, period, keys) -> EstimateMedianObjectList:
        result_json = self.get_median_bid_json(type, device, period, keys)
        estimate_list = []
        for arr in result_json:
            estimate = EstimateMedianObject(arr)
            estimate_list.append(estimate)
        return estimate_list

    def get_performance_json(self, type: str, device, keywordplus, key, bids):
        data = jsonpickle.encode(GetPerformanceObject(device, keywordplus, key, bids), unpicklable=False)
        data = json.loads(data)
        data = CommonFunctions.dropna(data)
        data_str = json.dumps(data)
        query = {'items': data_str}
        result = self.conn.post('/estimate/performance/' + type, data_str, query=query)
        result = result['estimate']
        return result

    def get_performance_list(self, type: str, device, keywordplus, key, bids) -> EstimatePerformanceObjectList:
        result_json = self.get_performance_json(type, device, keywordplus, key, bids)
        estimate_list = []
        for arr in result_json:
            estimate = EstimatePerformanceObject(arr)
            estimate_list.append(estimate)
        return estimate_list

    # def get_performance_many_json(self, type: str, GetPerformanceObjectList: GetPerformanceObjectList):
    #     data = jsonpickle.encode(GetPerformanceObjectList, unpicklable=False)
    #     data = json.loads(data)
    #     #data = CommonFunctions.dropna(data)
    #     data_str = json.dumps(data)
    #     print('data_str: ',data_str)
    #     result = self.conn.post('/estimate/performance/' + type, data_str)
    #     print('result: ',result)
    #     result = result['estimate']
    #     return result

    def get_performance_bulk_json(self, type: str, GetPerformanceBulkObjectList: GetPerformanceBulkObjectList):
        data = jsonpickle.encode(GetPerformanceBulkObjectList, unpicklable=False)
        data = json.loads(data)
        #data = CommonFunctions.dropna(data)
        data_str = json.dumps(data)
        print(data_str)
        result = self.conn.post('/estimate/performance-bulk', data_str)
        result = result['estimate']
        return result

    def get_performance_bulk_list(self, type: str, GetPerformanceObjectList: GetPerformanceObjectList):
        result_json = self.get_performance_bulk_json(type, GetPerformanceObjectList)
        estimate_list = []
        for arr in result_json:
            estimate = EstimatePerformanceObject(arr)
            estimate_list.append(estimate)
        return estimate_list
