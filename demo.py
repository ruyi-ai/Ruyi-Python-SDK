#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests

from optparse import OptionParser

if __name__ == '__main__':

    parser = OptionParser()
    parser.add_option("-k", "--app_key", dest = "app_key", help = "your appkey")

    (options, args) = parser.parse_args()
    assert options.app_key is not None, "app_key is missing"
    
    while True:
        q = raw_input("> ")
        payload = {'app_key': options.app_key, 'user_id': 'test_user_id', 'q': q}
        r = requests.get('http://api.ruyi.ai/v1/message', params=payload)
        response = json.loads(r.text)
    
        try:
            for output in response["result"]["intents"][0]["outputs"]:
    
                # wechat response
                if "type" in output and output["type"] == "wechat.text":
                    print "wechat response: " + output["property"]["text"]
    
                # other response
                if "type" in output and output["type"] == "dialog":
                    print "other response: " + output["property"]["text"]
     
        except:
            print "no intent or invalid app_key"
            pass
