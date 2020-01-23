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

class MasterReport:  # 광고정보일괄다운로드탭
    def __init__(self, base_url: str, api_key: str, secret_key: str, customer_id: int):
        self.conn = Connector(base_url, api_key, secret_key, customer_id)

    MasterReportObjectList = List[MasterReportObject]

    def get_master_report_list(self) -> MasterReportObjectList:
        result = self.conn.get('/master-reports')
        mreport_list = []
        for arr in result:
            mreport = MasterReportObject(arr)
            mreport_list.append(mreport)
        return mreport_list

    def get_master_report_by_id(self, id: str) -> MasterReportObject:
        result = self.conn.get('/master-reports/' + id)
        result = MasterReportObject(result)
        return result

    def create_master_report(self, CreateMasterReportObject: CreateMasterReportObject) -> MasterReportObject:
        data = jsonpickle.encode(CreateMasterReportObject, unpicklable=False)
        data = json.loads(data)
        data = CommonFunctions.dropna(data)
        data_str = json.dumps(data)
        result = self.conn.post('/master-reports', data_str)
        result = MasterReportObject(result)
        return result

    def delete_master_report_all(self):
        self.conn.delete('/master-reports')
        return True

    def delete_master_report_by_id(self, id: str):
        self.conn.delete('/master-reports', {'id': id})
        return True
