#!/usr/bin/env python
# -*- coding: utf-8 -*-
from test_wanitku.api.baseapi import BaseApi
from jsonpath import jsonpath
class Test_Papers(BaseApi):
    def test_getpapaerlist(self):
        req = {
            "method": "get",
            "url": self.host + "/api/question/GetPapers?pageIndex=1",
            "headers": self.headers
        }
        r = self.send_requests(req)
        assert r.json()["SubjectId"] == 44
        self.paperId = r.json()["EntityList"][0]["PaperId"]
        return (self.paperId)
    def test_getpapers(self):
        self.test_getpapaerlist()
        req = {
            "method": "get",
            "url":self.host + f"/api/question/Paper?paperId={self.paperId}&userExamPaperId=0",
            "headers": self.headers
        }
        r = self.send_requests(req)
        print(r.json())
        assert r.json()["Msg"] == "成功"
    def test_savepaper(self):
        self.test_getpapaerlist()
        req = {
            "method": "post",
            "url":self.host + "/API/report/SaveUserPaperWithQueue?",
            "json":{"paperid": self.paperId,"IsCheckinRewards": "false","isSavePaper": 1}
        }
        r = self.send_requests(req)
        self.SavePaperQueueId = r.json()["SavePaperQueueId"]
        print(self.SavePaperQueueId)
    def test_getuserexampaperid(self):
        self.test_savepaper()
        req ={
            "method":"get",
            "url":self.host + f"/api/report/GetRealUserExamPaperId?SavePaperQueueId={self.SavePaperQueueId}",
            "headers":self.headers,
        }
        r = self.send_requests(req)
        assert r.json()["Msg"] =="成功"
        self.userexampaperid = r.json()["UserExamPaperId"]
        print(self.userexampaperid)
        print(r.json())
    def test_analysis(self):
        self.test_getuserexampaperid()
        req = {
            "method": "get",
            "url":self.host + f"/api/question/Paper?paperId={self.paperId}&userExamPaperId={self.userexampaperid}",
            "headers": self.headers
        }
        r = self.send_requests(req)
        print(r.json())