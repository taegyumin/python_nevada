from nevada.Common.Connector import *
from typing import List
import json

class RelKwdStatObject:
    def __init__(self, json_def):
        if type(json_def) is str:
            s = json.loads(json_def)
        else:
            s = json_def
        self.relKeyword = None if 'relKeyword' not in s else s['relKeyword']
        self.monthlyPcQcCnt = None if 'monthlyPcQcCnt' not in s else s['monthlyPcQcCnt']
        self.monthlyMobileQcCnt = None if 'monthlyMobileQcCnt' not in s else s['monthlyMobileQcCnt']
        self.monthlyAvePcClkCnt = None if 'monthlyAvePcClkCnt' not in s else s['monthlyAvePcClkCnt']
        self.monthlyAveMobileClkCnt = None if 'monthlyAveMobileClkCnt' not in s else s['monthlyAveMobileClkCnt']
        self.monthlyAvePcCtr = None if 'monthlyAvePcCtr' not in s else s['monthlyAvePcCtr']
        self.monthlyAveMobileCtr = None if 'monthlyAveMobileCtr' not in s else s['monthlyAveMobileCtr']
        self.plAvgDepth = None if 'plAvgDepth' not in s else s['plAvgDepth']
        self.compIdx = None if 'compIdx' not in s else s['compIdx']

class RelKwdStat:
    def __init__(self, base_url: str, api_key: str, secret_key: str, customer_id: int):
        self.conn = Connector(base_url, api_key, secret_key, customer_id)

    RelKwdStatObjectList = List[RelKwdStatObject]

    def get_json(self, siteId: str = None, biztpId: int = None, hintKeywords: str = None, event: int = None,
                              month: int = None, showDetail: str = '1'):
        query = {'siteId': siteId,
                 'biztpId': biztpId,
                 'hintKeywords': hintKeywords,
                 'event': event,
                 'month': month,
                 'showDetail': showDetail
                 }
        result = self.conn.get(uri='/keywordstool', query=query)
        result = result['keywordList']
        return result

    def get_list(self, siteId: str = None, biztpId: int = None, hintKeywords: str = None, event: int = None,
                              month: int = None, showDetail: str = '1') -> RelKwdStatObjectList:
        result_json = self.get_json(siteId, biztpId, hintKeywords, event, month, showDetail)
        relstat_list = []
        for arr in result_json:
            relstat = RelKwdStatObject(arr)
            relstat_list.append(relstat)

        return relstat_list
