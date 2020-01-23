from nevada.Common.Connector import *
from typing import List
import jsonpickle
import json

class UpdateIpExclusionObject:
    def __init__(self, filterIp, ipFilterId, memo):
        self.filterIp = filterIp
        self.ipFilterId = ipFilterId
        self.memo = memo

class CreateIpExclusionObject:
    def __init__(self, filterIp, memo):
        self.filterIp = filterIp
        self.memo = memo

class IpExclusionObject:
    def __init__(self, json_def):
        if type(json_def) is str:
            json_def = json.loads(json_def)
        s = json_def
        self.customerId = None if 'customerId' not in s else s['customerId']
        self.filterIp = None if 'filterIp' not in s else s['filterIp']
        self.ipFilterId = None if 'ipFilterId' not in s else s['ipFilterId']
        self.memo = None if 'memo' not in s else s['memo']
        self.regTm = None if 'regTm' not in s else s['regTm']

class IpExclusion:
    def __init__(self, base_url: str, api_key: str, secret_key: str, customer_id: int):
        self.conn = Connector(base_url, api_key, secret_key, customer_id)

    ExclusionIdList = List[str]

    def get_ip_exclusion_json(self):
        result = self.conn.get('/tool/ip-exclusions')
        return result

    def get_ip_exclusion_list(self):
        result_list = self.get_ip_exclusion_json()
        ip_exclusion_list = []
        for arr in result_list:
            ipex = IpExclusionObject(arr)
            ip_exclusion_list.append(ipex)
        return ip_exclusion_list

    def create_ip_exclusion(self, filterIp, memo) -> IpExclusionObject:
        data = jsonpickle.encode(CreateIpExclusionObject(filterIp, memo), unpicklable=False)
        data = json.loads(data)
        data = CommonFunctions.dropna(data)
        data_str = json.dumps(data)
        result = self.conn.post('/tool/ip-exclusions', data_str)
        result = IpExclusionObject(result)
        return result

    def update_ip_exclusion(self, filterIp, ipFilterId, memo) -> UpdateIpExclusionObject:
        data = jsonpickle.encode(UpdateIpExclusionObject(filterIp, ipFilterId, memo), unpicklable=False)
        data = json.loads(data)
        data = CommonFunctions.dropna(data)
        data_str = json.dumps(data)
        result = self.conn.put('/tool/ip-exclusions', data_str)
        result = IpExclusionObject(result)
        return result

    def delete_ip_exclusion(self, id: str):
        result = self.conn.delete('/tool/ip-exclusions/' + id)
        result = IpExclusionObject(result)
        return result

    def delete_ip_exclusion_many(self, id_array: ExclusionIdList):
        query = {'ids':id_array}
        self.conn.delete('/tool/ip-exclusions', query)
        return True
