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

class StatReport:  #대용량 다운로드 보고서
    def __init__(self, base_url: str, api_key: str, secret_key: str, customer_id: int):
        self.conn = Connector(base_url, api_key, secret_key, customer_id)

    StatReportObjectList = List[StatReportObject]

    def list(self, format=True) -> StatReportObjectList:
        result = self.conn.get('/stat-reports')
        if format in [False, 'json']:
            return result
        elif format in [True, 'object', 'list']:
            stat_list = []
            for arr in result:
                stat = StatReportObject(arr)
                stat_list.append(stat)
            return stat_list
        else:
            print('Please Check the input value of format.')

    def get(self, reportJobId: str, format=True) -> StatReportObject:
        result = self.conn.get('/stat-reports/' + reportJobId)
        if format in [False, 'json']:
            return result
        elif format in [True, 'object', 'list']:
            return StatReportObject(result)
        else:
            print('Please Check the input value of format.')

    def create(self, reportTp, statDt, format=True) -> StatReportObject:
        data = jsonpickle.encode(CreateStatReportObject(reportTp, statDt), unpicklable=False)
        data = json.loads(data)
        data = CommonFunctions.dropna(data)
        data_str = json.dumps(data)
        result = self.conn.post('/stat-reports', data_str)
        if format in [False, 'json']:
            return result
        elif format in [True, 'object', 'list']:
            result = StatReportObject(result)
            return result
        else:
            print('Please Check the input value of format.')

    def delete_all(self):
        self.conn.delete('/stat-reports/')
        return True

    def delete_by_id(self, reportJobId: str):
        self.conn.delete('/stat-reports/' + reportJobId)
        return True
