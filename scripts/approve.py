import unittest
import requests
from api.Approve_Api import ApproveApi
import logging
from utils import assert_utils
from api.login_api import LoginApi


class Approve(unittest.TestCase):
    realname = "刘舰"
    CardId = "120102771101321"
    phone1 = "13636226185"
    phone2 = "13636226186"
    phone3 = "13636226187"

    pwd = "test001"


    def setUp(self) -> None:
        self.Approve_Api = ApproveApi()
        self.session = requests.session()
        self.login_api = LoginApi()

    def tearDown(self) -> None:
        self.session.close()

    def test001_approve_success(self):
        response = self.login_api.login_success(self.session, self.phone1, self.pwd)
        logging.info("login_success={}".format(response.json()))
        assert_utils(self, response, 200, 200, "登录成功")

        response = self.Approve_Api.approve(self.session, self.realname, self.CardId)
        logging.info("approve_success={}".format(response.json()))
        assert_utils(self, response, 200, 200, "提交成功!")

    def test002_name_null(self):
        response = self.login_api.login_success(self.session, self.phone2, self.pwd)
        logging.info("login_success={}".format(response.json()))
        assert_utils(self, response, 200, 200, "登录成功")

        response = self.Approve_Api.approve(self.session, " ", self.CardId)
        logging.info("approve_success={}".format(response.json()))
        assert_utils(self, response, 200, 100, "姓名不能为空")

    def test003_ID_number_is_null(self):
        response = self.login_api.login_success(self.session, self.phone2, self.pwd)
        logging.info("login_success={}".format(response.json()))
        assert_utils(self, response, 200, 200, "登录成功")

        response = self.Approve_Api.approve(self.session, self.realname, "")
        logging.info("approve_success={}".format(response.json()))
        assert_utils(self, response, 200, 100, "身份证号不能为空")

    def test004_get_apporve_success(self):
        response = self.login_api.login_success(self.session, self.phone1, self.pwd)
        logging.info("login_success={}".format(response.json()))
        assert_utils(self, response, 200, 200, "登录成功")

        response = self.Approve_Api.getapprove(self.session)
        logging.info("getapprove ={}".format(response.json()))
        self.assertEqual(200, response.status_code)





