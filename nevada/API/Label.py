from nevada.Common.Connector import *
from typing import List
import jsonpickle
import json

class UpdateLabelObject:
    def __init__(self, color, name, nccLabelId):
        self.color = color
        self.name = name
        self.nccLabelId = nccLabelId

class LabelObject:
    def __init__(self, json_def):
        if type(json_def) is str:
            json_def = json.loads(json_def)
        s = json_def
        self.color = None if 'color' not in s else s['color']
        self.customerId = None if 'customerId' not in s else s['customerId']
        self.editTm = None if 'editTm' not in s else s['editTm']
        self.name = None if 'name' not in s else s['name']
        self.nccLabelId = None if 'nccLabelId' not in s else s['nccLabelId']
        self.regTm = None if 'regTm' not in s else s['regTm']

class Label:
    def __init__(self, base_url: str, api_key: str, secret_key: str, customer_id: int):
        self.conn = Connector(base_url, api_key, secret_key, customer_id)

    LabelObjectList = List[LabelObject]

    def get_label_json(self):
        result = self.conn.get('/ncc/labels')
        return result

    def get_label_list(self) -> LabelObjectList:
        result = self.get_label_json()
        label_list = []
        for arr in result:
            label = LabelObject(arr)
            label_list.append(label)
        return label_list

    def update_label(self, color:str, name:str, nccLabelId:str) -> LabelObject:
        data = jsonpickle.encode(UpdateLabelObject(color, name, nccLabelId), unpicklable=False)
        data = json.loads(data)
        data = CommonFunctions.dropna(data)
        data_str = json.dumps(data)
        result = self.conn.put('/ncc/labels', data_str)
        result = LabelObject(result)
        return result
