from nevada.Common.Connector import *
from typing import List
import jsonpickle
import json

class CreateStatReportObject:
    def __init__(self, reportTp, statDt):
        self.reportTp = reportTp
        self.statDt = statDt

class StatReportObject:
    def __init__(self, json_def):
        if type(json_def) is str:
            json_def = json.loads(json_def)
        s = json_def
        self.downloadUrl = None if 'downloadUrl' not in s else s['downloadUrl']
        self.loginId = None if 'loginId' not in s else s['loginId']
        self.regTm = None if 'regTm' not in s else s['regTm']
        self.reportJobId = None if 'reportJobId' not in s else s['reportJobId']
        self.reportTp = None if 'reportTp' not in s else s['reportTp']
        self.statDt = None if 'statDt' not in s else s['statDt']
        self.status = None if 'status' not in s else s['status']
        self.updateTm = None if 'updateTm' not in s else s['updateTm']

class StatReport:  # 대용량 보고서
    def __init__(self, base_url: str, api_key: str, secret_key: str, customer_id: int):
        self.conn = Connector(base_url, api_key, secret_key, customer_id)

    StatReportObjectList = List[StatReportObject]

    def get_stat_report_list(self) -> StatReportObjectList:
        result = self.conn.get('/stat-reports')
        stat_list = []
        for arr in result:
            stat = StatReportObject(arr)
            stat_list.append(stat)
        return stat_list

    def get_stat_report(self, reportJobId: str) -> StatReportObject:
        result = self.conn.get('/stat-reports/' + reportJobId)
        result = StatReportObject(result)
        return result

    def create_stat_report(self, CreateStatReportObject: CreateStatReportObject) -> StatReportObject:
        data = jsonpickle.encode(CreateStatReportObject, unpicklable=False)
        data = json.loads(data)
        data = CommonFunctions.dropna(data)
        data_str = json.dumps(data)

        result = self.conn.post('/stat-reports', data_str)
        result = StatReportObject(result)
        return result

    def delete_stat_reports(self, reportJobId: str):
        self.conn.delete('/stat-reports/' + reportJobId)
        return True
