#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests

headers ={
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
data_url = "https://weixin.566.com//api/login/EncryptMobile?"
data = {"mobile" :"18600215696"}
r = requests.get(url=data_url,params=data,headers =headers)
# assert r.json()["Msg"] == "成功"
print(r.json())
