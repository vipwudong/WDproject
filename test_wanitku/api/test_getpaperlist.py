#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests

from test_wanitku.api.baseapi import BaseApi


class Test_Paperlist(BaseApi):
    def test_getpapaerlist(self):
        req = {
            "method": "get",
            "url": "https://weixin.566.com//api/question/GetPapers?pageIndex=1",
            "headers": self.headers
        }
        r = self.send_requests(req)
        assert r.json()["SubjectId"] == 44
        self.paperId = r.json()["EntityList"][0]["PaperId"]
        return (self.paperId)
