import random
import unittest
import requests
import logging
from bs4 import BeautifulSoup
from utils import assert_utils, request_third_account
from api.login_api import LoginApi
from api.account_api import AccountApi


class Account(unittest.TestCase):
    phone1 = "13636226185"
    pwd = "test001"

    def setUp(self) -> None:
        self.account_api = AccountApi()
        self.login_api = LoginApi()
        self.session = requests.session()

    def tearDown(self) -> None:
        self.session.close()

    def test001_open_account_success(self):
        #认证通过的登录账户
        response = self.login_api.login_success(self.session, self.phone1, self.pwd)
        logging.info("login_success={}".format(response.json()))
        assert_utils(self, response, 200, 200, "登录成功")

        # 发送开户请求
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

    def test002_get_verify_code_random_float(self):
        r = random.random()
        response = self.login_api.get_VerifyCode(self.session, str(r))
        self.assertEqual(200, response.status_code)

    def test003_get_verify_code_random_integers(self):
        r = random.randint(1000000, 9000000)
        response = self.login_api.get_VerifyCode(self.session, str(r))
        self.assertEqual(200, response.status_code)

    def test004_get_verify_code_num_null(self):
        response = self.login_api.get_VerifyCode(self.session, "")
        self.assertEqual(404, response.status_code)

    def test005_get_verify_code_is_char(self):
        r = random.sample("abcdefc", 7)
        rand = "".join(r)
        logging.info(rand)
        response = self.login_api.get_VerifyCode(self.session, rand)
        self.assertEqual(400, response.status_code)

    def test006_charge_success(self):
        response = self.login_api.login_success(self.session, self.phone1, self.pwd)
        logging.info("login_success={}".format(response.json()))
        assert_utils(self, response, 200, 200, "登录成功")

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












