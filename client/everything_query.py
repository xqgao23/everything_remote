#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request
import sys
import json

class Everything_Search:
    
    def __init__(self, url, user, pwd):
        self.url = url
        self.user = user
        self.pwd = pwd

        pwd_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
        pwd_mgr.add_password(None, self.url, self.user, self.pwd)
        handler = urllib.request.HTTPBasicAuthHandler(pwd_mgr)
        self.opener = urllib.request.build_opener(handler)
    
    def query(self, q, c):
        q = urllib.parse.quote(q)
        q_url = self.url + '?s=' + q + '&j=1&path_column=1&size_column=1&date_modified_column=1&c=' + str(c)
        info = json.loads(self.opener.open(q_url).read().decode('utf8'))
        result_counts = info['totalResults']
        result = info['results']
        print("<?xml version=\"1.0\"?>\n<items>")
        for item in result:
            print("    <item uid=\"everything remote\" arg=\"" + item['path'] + "\\" + item['name'] + "\">")
            print("        <title>" + item['name'] + "</title>")
            print("        <subtitle>" + item['path'] + "</subtitle>")
            print("        <icon>everything.png</icon> </item>")
        print("</items>\n")
        

if __name__ == '__main__':
    url = 'http://xxx.xxx.xxx.xxx:xxxx/'
    user = 'xx'
    pwd = 'xxxx'
    counts = 10

    if len(sys.argv) > 1:
        q = sys.argv[1]
        search = Everything_Search(url, user, pwd)
        search.query(q, counts)
