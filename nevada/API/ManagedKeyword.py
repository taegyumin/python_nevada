from nevada.Common.Connector import *
from typing import List
import jsonpickle
import json

class ManagedKeywordInfoObject:
    def __init__(self, json_def):
        if type(json_def) is str:
            json_def = json.loads(json_def)
        s = json_def
        self.PCPLMaxDepth = None if 'PCPLMaxDepth' not in s else s['PCPLMaxDepth']
        self.editTm = None if 'editTm' not in s else s['editTm']
        self.isAdult = None if 'isAdult' not in s else s['isAdult']
        self.isBrand = None if 'isBrand' not in s else s['isBrand']
        self.isLowSearchVolume = None if 'isLowSearchVolume' not in s else s['isLowSearchVolume']
        self.isRestricted = None if 'isRestricted' not in s else s['isRestricted']
        self.isSeason = None if 'isSeason' not in s else s['isSeason']
        self.isSellProhibit = None if 'isSellProhibit' not in s else s['isSellProhibit']
        self.keyword = None if 'keyword' not in s else s['keyword']
        self.regTm = None if 'regTm' not in s else s['regTm']

class ManagedKeywordObject:
    def __init__(self, json_def):
        if type(json_def) is str:
            json_def = json.loads(json_def)
        s = json_def
        self.keyword = None if 'keyword' not in s else s['keyword']
        self.managedKeyword = None if 'managedKeyword' not in s else ManagedKeywordInfoObject(s['managedKeyword'])

class ManagedKeyword:
    def __init__(self, base_url: str, api_key: str, secret_key: str, customer_id: int):
        self.conn = Connector(base_url, api_key, secret_key, customer_id)

    KeywordsList = List[str]

    def list_by_keywords(self, keywords: KeywordsList) -> ManagedKeywordObject:
        keywords = ",".join(keywords)
        query = {'keywords': keywords}
        result = self.conn.get('/ncc/managedKeyword', query)
        return result
