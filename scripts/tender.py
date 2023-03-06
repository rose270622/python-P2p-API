import logging
import unittest

import requests

from api.login_api import LoginApi
from api.tender_api import TenderApi
from utils import assert_utils,request_third_account


class Tender(unittest.TestCase):
    phone1 = "19972299985"
    pwd = "wyl123456"
    def setUp(self) -> None:
        self.tender_api = TenderApi()
        self.session = requests.session()
        self.login_api = LoginApi()

    def tearDown(self) -> None:
        self.session.close()

    def test001_get_loan_info_success(self):
        response = self.tender_api.loan(self.session)
        logging.info("tender_api.loan={}".format(response.json()))
        self.assertEquals(200, response.status_code)
        self.assertEquals(200, response.json().get("status"))


    def test002_id_error(self):
        response = self.tender_api.loan(self.session, id="11")
        logging.info("tender_api.loan={}".format(response.json()))
        self.assertEquals(200, response.status_code)
        self.assertEquals(100, response.json().get("status"))

    def test003_id_null(self):
        response = self.tender_api.loan(self.session, " ")
        logging.info("tender_api.loan={}".format(response.json()))
        self.assertEquals(200, response.status_code)
        self.assertEquals(100, response.json().get("status"))

    def test004_all_params_success(self):
        response = self.login_api.login_success(self.session, self.phone1, self.pwd)
        logging.info("login_success={}".format(response.json()))
        assert_utils(self, response, 200, 200, "登录成功")

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


