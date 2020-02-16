import json
import time
import hmac
import base64
import hashlib
import requests
import urllib.parse
from datetime import datetime

class CommonFunctions:

    @staticmethod
    def print_all_attr(obj: object):
        type_list = [type(True), type('str'), type(0), type(None), type({'0':0}), type(0.1)]

        def print_all_attr_copy(obj: object, temp):
            for key in obj.__dict__.keys():
                if temp == 1:
                    print(' L  ', end='')
                elif temp == 2:
                    print('     L  ', end='')
                elif temp == 3:
                    print('         L  ', end='')

                print(key, ': ', end='')

                if type(obj.__getattribute__(key)) in type_list:
                    print(obj.__getattribute__(key))
                else:
                    print()
                    temp += 1
                    print_all_attr_copy(obj.__getattribute__(key), temp)
                    temp -= 1

        print_all_attr_copy(obj, 0)
        print()

    @staticmethod
    def dropna(input_dict):
        cleaned_dict = dict()
        for now in input_dict:
            if input_dict[now] != None:
                cleaned_dict.update({now: input_dict[now]})
        return cleaned_dict

    # def dropna(self, input_dict):
    #     cleaned_dict = dict()
    #     for now in input_dict:
    #         if type(input_dict[now])==type({'j':'son'}):
    #             temp = dict()
    #             for now2 in now:
    #                 if now[now2] != None:
    #                     temp.update({now2: now[now2]})
    #             cleaned_dict.update({now: temp})
    #         else:
    #             cleaned_dict.update({now: input_dict[now]})
    #     return cleaned_dict

class Connector:
    def __init__(self, base_url, api_key, secret_key, customer_id):
        self.base_url = base_url
        self.api_key = api_key
        self.secret_key = secret_key
        self.customer_id = customer_id

    def help(self):
        import Help
        help_message = Help.Connector
        print(help_message)
        return help_message

    def generate_signature(self, timestamp, method, path):
        sign = '{timestamp}.{method}.{path}'.format(timestamp=timestamp, method=method, path=path)
        signature = hmac.new(self.secret_key.encode(), sign.encode(), hashlib.sha256).digest() #.hexdigest()
        return base64.b64encode(signature).decode()

    def build_http_query(self, query):
        if query:
            query_list = []
            for key, value in query.items():
                if value != None:
                    if (type(value)==type([])) and len(value)!=1:
                        for i in value:
                            q = "{key}={value}".format(key=urllib.parse.quote_plus(key),value=urllib.parse.quote_plus(i))
                            query_list.append(q)
                    else:
                        q = "{key}={value}".format(key=urllib.parse.quote_plus(key),value=urllib.parse.quote_plus(value))
                        query_list.append(q)
            return '&'.join(query_list)
        else:
            return ''

    def get_header(self, method, uri):
        timestamp = self.get_timestamp()
        header = {}
        header['Content-Type'] = 'application/json; charset=UTF-8'
        header['X-Timestamp'] = str(timestamp)
        header['X-API-KEY'] = self.api_key
        header['X-Customer'] = str(self.customer_id)
        header['X-Signature'] = self.generate_signature(timestamp, method, uri)
        return header

    def get_transaction_id(self, headers):
        if "X-Transaction-ID" in headers:
            return headers["X-Transaction-ID"]
        else:
            return "unknown"

    def parse_response(self, response):
        if response:
            header = response.headers
            body = response.text
            transaction_id = self.get_transaction_id(header)
            json_body = json.loads(body)

            return {'transaction_id': transaction_id, 'json': json_body}

        return {}

    def get(self, uri, query={}):
        url = "{base_url}{uri}{query}{http_query}".format(
            base_url=self.base_url,
            uri=uri,
            query='' if query == {} else '?',
            http_query=self.build_http_query(query))
        headers = self.get_header('GET', uri)

        try:
            r = requests.get(url=url, headers=headers)
            response = self.parse_response(r)
            if not r.ok:
                print("Http status: {status_code}".format(status_code=r.status_code))
            return response['json']
        except:
            print("failed to request")

    def post(self, uri, data, query={}):
        url = "{base_url}{uri}{query}{http_query}".format(
            base_url=self.base_url,
            uri=uri,
            query='' if query == {} else '?',
            http_query=self.build_http_query(query))
        headers = self.get_header('POST', uri)
        try:
            r = requests.post(url=url, data=data, headers=headers)
            response = self.parse_response(r)
            if not r.ok:
                print("Http status: {status_code}".format(status_code=r.status_code))
            return response['json']
        except:
            print("failed to request")

    def put(self, uri, data, query={}):
        url = "{base_url}{uri}{query}{http_query}".format(
            base_url=self.base_url,
            uri=uri,
            query='' if query == {} else '?',
            http_query=self.build_http_query(query))

        headers = self.get_header('PUT', uri)

        try:
            r = requests.put(url=url, data=data, headers=headers)
            response = self.parse_response(r)
            if not r.ok:
                print("Http status: {status_code}".format(status_code=r.status_code))
            return response['json']
        except:
            print("failed to request")

    def delete(self, uri, query={}):
        url = "{base_url}{uri}{query}{http_query}".format(
            base_url=self.base_url,
            uri=uri,
            query='' if query == {} else '?',
            http_query=self.build_http_query(query))

        headers = self.get_header('DELETE', uri)

        try:
            r = requests.delete(url=url, headers=headers)
            response = self.parse_response(r)
            if not r.ok:
                print("Http status: {status_code}".format(status_code=r.status_code))
            return response['json']
        except:
            print("failed to request")

    def get_timestamp(self):
        return round(time.time() * 1000)

    def get_datetime(self):
        return datetime.now()

    def download(self, url, localpath):
        return None

    def null_dict(self, input_dict):
        real = dict()
        for now in input_dict:
            if input_dict[now] != None:
                real.update({now :input_dict[now]})
        return real
