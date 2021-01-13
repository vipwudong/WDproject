#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
class LogIn:
    def __init__(self):
         self.headers ={
            "UserClientType": "102",
            "FakesubjectParentId": "0",
            "SubjectId": "634",
            "OpenId": "ouoD50BJyntZYO_P4nKD7zpK7pjA",
            "SubjectMergerId": "538",
            "SubjectParentId": "549",
            "PackageId": "1",
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1 wechatdevtools/1.04.2006192 MicroMessenger/7.0.4 Language/zh_CN webview/",
            "SubjectLevel": "31",
            "VersionReview": "180",
            "VersionNumber": "3630",
            "Token": "20210113173647-e1d6dc0525d7992986f7d6603c916942"
            }
    def test_data(self):
        data_url = "https://weixin.566.com//api/login/EncryptMobile?"
        data = {"mobile" :"18600215696"}
        r = requests.get(url=data_url,params=data,headers=self.headers)
        assert r.json()["Msg"] == "成功"
        print(r.json())
    def test_login(self):
        login_url = "https://weixin.566.com//api/login/MobileLogin?t=1610525122000"
        login_data = {"encryptedData": "KKpixBVRDkl2H9an6Sq5wWayyQUf/28xkP+JSnTCjHWpoB2cOcoTyLKuRHV9kKg4lQicNj8+9K2RZ3JJH3LH8KkSa7c9nXroos008M1S0+rRzsZh+PPm4E/tKmKdGS3Vt6KroOk+wU9BZmYtYsq2SJv4LJdKDYPvA8MW1Y1N66x5gHmNYP5job8pqEVXPv40N5E+GE6mv1JXBUITvF+HSA==","iv": "b/Ok0mdF9rzWGCrR3vQvHQ=="}
        r = requests.post(url=login_url,data=login_data,headers=self.headers)
        print(r.json())
        assert r.json()["NickName"] == "刘全有"
