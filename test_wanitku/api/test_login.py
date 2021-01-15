#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests

from test_wanitku.api.baseapi import BaseApi


class TestLogin(BaseApi):
    def setup_class(self):
        req = {
            "method" : "get",
            "url":"https://weixin.566.com//api/login/EncryptMobile?",
            "params":{"mobile": "18600215696"},
            "headers":self.headers
        }
        r = self.send_requests(self,req)
        self.data_login = r.json()["Data"]
        return self.data_login

    def test_login(self):
        req = {
            "method": "post",
            "url": "https://weixin.566.com//api/login/MobileLogin?",
            "data": self.data_login,
            "headers": self.headers}
        r = self.send_requests(req)
        assert r.json()["NickName"] == "刘全有"
        print(r.json())
