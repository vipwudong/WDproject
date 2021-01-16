#!/usr/bin/env python
# -*- coding: utf-8 -*-
from jsonpath import jsonpath

from test_wanitku.api.baseapi import BaseApi


class TestZhangjielianxi(BaseApi):
    def test_GetSpecialIntelligenceTree(self):
        req = {
            "method": "get",
            "url": self.host + "/api/question/GetSpecialIntelligenceTree?",
            "headers": {"SubjectId": "436",
                        "UserId": "6648816",
                        "SubjectParentId": "435",
                        "PackageId": "1",
                        "Token": "20210115135342-ec41f8dc0cd97c2822534678894671f4"
                        }
        }
        r = self.send_requests(req)
        print(r.json())
        self.ExamSiteId = r.json()["SiteQuestionUserList"][0]["ExamSiteId"]
        print(self.ExamSiteId)
    def test_SpecialExercisePaper(self):
        self.test_GetSpecialIntelligenceTree()
        req = {
            "method": "get",
            "url": self.host + f"//api/question/SpecialExercisePaper?examSiteId={self.ExamSiteId}",
            "headers": {"SubjectId": "436",
                        "UserId": "6648816",
                        "SubjectParentId": "435",
                        "PackageId": "1",
                        "Token": "20210115135342-ec41f8dc0cd97c2822534678894671f4"
                        }
        }
        r = self.send_requests(req)
        print(r.json())
        list = jsonpath(r,"&..QuestionId")
        print(list)