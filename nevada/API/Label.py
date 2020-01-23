from nevada.Common.Connector import *
from typing import List
import jsonpickle
import json

class UpdateLabelObject:
    def __init__(self, nccLabelId):
        self.color = None
        self.name = None
        self.nccLabelId = nccLabelId

class UpdateLabelRefObject:
    def __init__(self, customerId, nccLabelId, refId, refTp):
        self.customerId = customerId
        self.enable = True
        self.nccLabelId = nccLabelId
        self.refId = refId
        self.refTp = refTp

class LabelRefObject:
    def __init__(self, json_def):
        if type(json_def) is str:
            json_def = json.loads(json_def)
        s = json_def
        self.nccLabelId = None if 'nccLabelId' not in s else s['nccLabelId']
        self.customerId = None if 'customerId' not in s else s['customerId']
        self.refId = None if 'refId' not in s else s['refId']
        self.refTp = None if 'refTp' not in s else s['refTp']
        self.enable = None if 'enable' not in s else s['enable']

class LabelObject:
    def __init__(self, json_def):
        if type(json_def) is str:
            json_def = json.loads(json_def)
        s = json_def
        self.color = None if 'color' not in s else s['color']
        self.customerId = None if 'customerId' not in s else s['customerId']
        self.name = None if 'name' not in s else s['name']
        self.nccLabelId = None if 'nccLabelId' not in s else s['nccLabelId']
        self.regTm = None if 'regTm' not in s else s['regTm']
        self.editTm = None if 'editTm' not in s else s['editTm']


class Label: #즐겨찾기
    def __init__(self, base_url: str, api_key: str, secret_key: str, customer_id: int):
        self.conn = Connector(base_url, api_key, secret_key, customer_id)

    LabelRefObjectList = List[LabelRefObject]
    LabelObjectList = List[LabelObject]

    def get_label_list(self) -> LabelObjectList:
        result = self.conn.get('/ncc/labels')

        label_list = []
        for arr in result:
            label = LabelObject(arr)
            label_list.append(label)

        return label_list

    def update_label(self, UpdateLabelObject: UpdateLabelObject) -> LabelObject:
        data = jsonpickle.encode(UpdateLabelObject, unpicklable=False)
        data = json.loads(data)
        data = CommonFunctions.dropna(data)
        data_str = json.dumps(data)

        result = self.conn.put('/ncc/labels', data_str)

        result = LabelObject(result)

        return result

    def update_label_ref(self, UpdateLabelRefObject: UpdateLabelRefObject) -> LabelRefObjectList:
        data = jsonpickle.encode(UpdateLabelRefObject, unpicklable=False)
        data = json.loads(data)
        data = CommonFunctions.dropna(data)
        data = [data]
        data_str = json.dumps(data)

        result = self.conn.put('/ncc/label-refs/', data_str)

        labelref_list = []
        for arr in result:
            labelref = LabelRefObject(arr)
            labelref_list.append(labelref)

        return labelref_list
