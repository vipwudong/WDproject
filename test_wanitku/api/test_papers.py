#!/usr/bin/env python
# -*- coding: utf-8 -*-
from test_wanitku.api.baseapi import BaseApi
from test_wanitku.api.test_getpaperlist import Test_Paperlist

class Test_Papers(Test_Paperlist):

    def test_getpapers(self):
        super(Test_Papers, self).test_getpapaerlist()
        paperid =self.paperId
        req = {
            "method": "get",
            "url": f"https://weixin.566.com//api/question/Paper?t=1610695930000&paperId={paperid}&userExamPaperId=0",
            "headers": self.headers
        }
        r = self.send_requests(req)
        print(r.json())
        # assert r.json()

