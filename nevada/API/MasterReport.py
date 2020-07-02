from nevada.Common.Connector import *
from typing import List
import jsonpickle
import json

class CreateMasterReportObject:
    def __init__(self, item, fromTime):
        self.item = item
        self.fromTime = fromTime

class MasterReportObject:
    def __init__(self, json_def):
        if type(json_def) is str:
            json_def = json.loads(json_def)
        s = json_def
        self.clientCustomerId = None if 'clientCustomerId' not in s else s['clientCustomerId']
        self.downloadUrl = None if 'downloadUrl' not in s else s['downloadUrl']
        self.fromTime = None if 'fromTime' not in s else s['fromTime']
        self.id = None if 'id' not in s else s['id']
        self.item = None if 'item' not in s else s['item']
        self.managerCustomerId = None if 'managerCustomerId' not in s else s['managerCustomerId']
        self.managerLoginId = None if 'managerLoginId' not in s else s['managerLoginId']
        self.registTime = None if 'registTime' not in s else s['registTime']
        self.status = None if 'status' not in s else s['status']
        self.updateTime = None if 'updateTime' not in s else s['updateTime']

class MasterReport: #광고 정보 일괄 다운로드
    def __init__(self, base_url: str, api_key: str, secret_key: str, customer_id: int):
        self.conn = Connector(base_url, api_key, secret_key, customer_id)

    MasterReportObjectList = List[MasterReportObject]

    def list(self) -> MasterReportObjectList:
        result = self.conn.get('/master-reports')
        return result

    def get_by_id(self, id:str) -> MasterReportObject:
        result = self.conn.get('/master-reports/' + id)
        return result

    def create(self, item:str, fromTime:str) -> MasterReportObject:
        data = jsonpickle.encode(CreateMasterReportObject(item, fromTime), unpicklable=False)
        data = json.loads(data)
        data = CommonFunctions.dropna(data)
        data_str = json.dumps(data)
        result = self.conn.post('/master-reports', data_str)
        return result

    def delete_all(self):
        self.conn.delete('/master-reports')
        return True

    def delete_by_id(self, id: str):
        self.conn.delete('/master-reports/'+id)
        return True