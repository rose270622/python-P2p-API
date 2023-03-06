import logging
import random
import unittest

import app
import pymysql

import requests

from api.Approve_Api import ApproveApi
from api.account_api import AccountApi
from api.login_api import LoginApi
from api.tender_api import TenderApi
from utils import assert_utils, request_third_account,DBuitls


class TenderProcess(unittest.TestCase):
    phone1 = "13636226110"
    pwd = "test123"
    img_code ="8888"
    @classmethod
    def setUp(cls) -> None:
        cls.login_api = LoginApi()
        cls.account_api = AccountApi()
        cls.approve_api = ApproveApi()
        cls.tender_api = TenderApi()
        cls.session = requests.session()

    @classmethod
    def tearDown(cls) -> None:
        cls.session.close()
        sql1="delete  i. *from mb_member_info   i inner  join mb_member  m on i.member_id=m.id where m.phone in( '13636226185','13636226186','13636226187','13636226188','13636226110');"
        DBuitls.delete(app.DB_MEMBER, sql1)
        logging.info("delete sql1={}".format(sql1))
        sql2="delete  l.* from  mb_member_login_log  l  inner  join mb_member m on l.member_id=m.id where m.phone in( '13636226185','13636226186','13636226187','13636226188','13636226110');"
        DBuitls.delete(app.DB_MEMBER, sql2)
        logging.info("delete sql2={}".format(sql2))
        sql3="delete*from mb_member_register-Log where phone in( '13636226185','13636226186','13636226187','13636226188','13636226110');"
        DBuitls.delete(app.DB_MEMBER, sql3)
        logging.info("delete sql3={}".format(sql3))
        sql4="delete*from mb_member  where phone in( '13636226185','13636226186','13636226187','13636226188','13636226110');"
        DBuitls.delete(app.DB_MEMBER, sql4)
        logging.info("delete sql4={}".format(sql4))

    def test001_tender_process(self):
        r = random.random()
        response = self.login_api.get_VerifyCode(self.session, str(r))
        self.assertEqual(200, response.status_code)

        response = self.login_api.get_sms_code(self.session, self.phone1, self.img_code, )
        logging.info("get_sms_code={}".format(response.json()))
        assert_utils(self, response, 200, 200, "短信发送成功")

        response = self.login_api.register(self.session, self.phone1, self.pwd)
        logging.info("register_success={}".format(response.json()))
        assert_utils(self, response, 200, 200, "注册成功")

        response = self.login_api.login_success(self.session, self.phone1, self.pwd)
        logging.info("login_success={}".format(response.json()))
        assert_utils(self, response, 200, 200, "登录成功")

        response = self.account_api.open_account(self.session)
        logging.info("open_account={}".format(response.json()))
        self.assertEquals(200, response.status_code)
        self.assertEquals(200, response.json().get("status"))
        # 发送第三方开户请求
        # 获取表单数据
        form_data = response.json().get("description").get("form")
        logging.info("form_data_response={}".format(response.json()))

        response = request_third_account(form_data)
        self.assertEqual(200, response.status_code)
        self.assertEqual("UserRegister OK", response.text)

        r = random.random()
        response = self.login_api.get_VerifyCode(self.session, str(r))
        self.assertEqual(200, response.status_code)

        response = self.account_api.recharge(self.session)
        logging.info("recharge={}".format(response.json()))
        self.assertEquals(200, response.status_code)
        self.assertEquals(200, response.json().get("status"))

        form_data = response.json().get("description").get("form")
        logging.info("form_data={}".format(response.json()))

        response = request_third_account(form_data)
        self.assertEqual(200, response.status_code)
        self.assertEqual("NetSave OK", response.text)

        response = self.tender_api.tender(self.session)
        logging.info("tender={}".format(response.json()))
        self.assertEquals(200, response.status_code)
        self.assertEquals(200, response.json().get("status"))

        form_data = response.json().get("description").get("form")
        logging.info("from_data={}".format(response.json()))
        response = request_third_account(form_data)
        self.assertEqual(200, response.status_code)
        self.assertEqual("InitiativeTender OK", response.text)

        response = self.tender_api.tender_list(self.session)
        logging.info("tender_list={}".format(response.json()))


