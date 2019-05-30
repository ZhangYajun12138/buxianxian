# coding:utf-8

from common.jsonp_to_json import jsonp_to_json
from common.launch_brower import launch_brower
import re
import requests

class Fund:

    fund_api_url = '接口地址url'

    def api_startegy(self,day = ''): # 接口1
        url = Fund.fund_api_url + 'api1.json'
        response = requests.get(url,params={'day':day}).json()
        return  response

    def api_lastestinfo(self,code): # 接口2
        url = Fund.fund_api_url + 'lastestInFo/{0}.json'.format(code)
        response = requests.get(url).json()
        return response

    def api_trends(self,code,pattern,period): # 接口3
        identifier = "{code}_{pattern}_{period}".format(code=code, pattern=pattern, period=period)
        url = Fund.fund_api_url + "trends/{0}.json".format(identifier)
        jsonpstr = requests.get(url).text
        jsonstr = jsonp_to_json(jsonpstr)
        return jsonstr

    def api_timeline(self, code): # 接口4
        url = Fund.fund_api_url + "timeline/{0}.json".format(code)
        response = requests.get(url).json()
        return response