import unittest
from api.login_api import LoginApi
import random
import logging
import requests
from utils import assert_utils
import time



class Login(unittest.TestCase):
    phone1 = "login.py"
    pwd = "test001"
    img_code = "8888"
    sms_code = "666666"
    phone2 = "13636226186"
    phone3 = "13636226187"
    phone4 = "13636226188"





    def setUp(self) -> None:
        self.login_api = LoginApi()
        self.session = requests.session()

    def tearDown(self) -> None:
        self.session.close()

    def test001_get_verify_code_random_float(self):
        r = random.random()
        response = self.login_api.get_VerifyCode(self.session, str(r))
        self.assertEqual(200, response.status_code)

    def test002_get_verify_code_random_integers(self):
        r = random.randint(1000000, 9000000)
        response = self.login_api.get_VerifyCode(self.session, str(r))
        self.assertEqual(200, response.status_code)

    def test003_get_verify_code_num_null(self):
        response = self.login_api.get_VerifyCode(self.session, "")
        self.assertEqual(404, response.status_code)

    def test004_get_verify_code_is_char(self):
        r = random.sample("abcdefc", 7)
        rand = "".join(r)
        logging.info(rand)
        response = self.login_api.get_VerifyCode(self.session, rand)
        self.assertEqual(400, response.status_code)

    def test005_get_sms_code_success(self):
        # 定义参数(随机小数)
        r = random.random()
        # 调用接口类中的接口
        response = self.login_api.get_VerifyCode(self.session, str(r))
        # 接收接口的返回结果，进行断言
        self.assertEqual(200, response.status_code)

        response = self.login_api.get_sms_code(self.session, self.phone1, self.img_code)
        logging.info("get_sms_code={}".format(response.json()))
        # self.assertEqual(200, response.status_code)
        # self.assertEqual(200, response.json().get("status"))
        # self.assertIn("短信发送成功", response.json().get("description"))
        assert_utils(self, response, 200, 200, "短信发送成功")

    def test006_img_code_error(self):
        r = random.random()
        # 调用接口类中的接口
        response = self.login_api.get_VerifyCode(self.session, str(r))
        # 接收接口的返回结果，进行断言
        self.assertEqual(200, response.status_code)
        response = self.login_api.get_sms_code(self.session, self.phone1, "88")
        logging.info("get_sms_code={}".format(response.json()))
        assert_utils(self, response, 200, 100, "图片验证码错误")

    def test007_phone_number_null(self):
        r = random.random()
        # 调用接口类中的接口
        response = self.login_api.get_VerifyCode(self.session, str(r))
        # 接收接口的返回结果，进行断言
        self.assertEqual(200, response.status_code)
        response = self.login_api.get_sms_code(self.session, "", self.img_code)
        logging.info("get_sms_code={}".format(response.json()))
        self.assertEqual(200, response.status_code)
        self.assertEqual(100, response.json().get("status"))

    def test008_img_code_null(self):
        r = random.random()
        # 调用接口类中的接口
        response = self.login_api.get_VerifyCode(self.session, str(r))
        # 接收接口的返回结果，进行断言
        self.assertEqual(200, response.status_code)
        response = self.login_api.get_sms_code(self.session, self.phone1, "")
        logging.info("get_sms_code={}".format(response.json()))
        assert_utils(self, response, 200, 100, "图片验证码错误")

    def test009_part_params_success(self):
        r = random.random()
        response = self.login_api.get_VerifyCode(self.session, str(r))
        self.assertEqual(200, response.status_code)

        response = self.login_api.get_sms_code(self.session, self.phone1, self.img_code,)
        logging.info("get_sms_code={}".format(response.json()))
        assert_utils(self, response, 200, 200, "短信发送成功")

        response = self.login_api.register(self.session, self.phone1, self.pwd)
        logging.info("register_success={}".format(response.json()))
        assert_utils(self, response, 200, 200, "注册成功")

    def test010_all_params_success(self):
        r = random.random()
        response = self.login_api.get_VerifyCode(self.session, str(r))
        self.assertEqual(200, response.status_code)

        response = self.login_api.get_sms_code(self.session, self.phone2, self.img_code,)
        logging.info("get_sms_code={}".format(response.json()))
        assert_utils(self, response, 200, 200, "短信发送成功")

        response = self.login_api.register(self.session, self.phone2, self.pwd, invitephone="18371912089")
        logging.info("register_success={}".format(response.json()))
        assert_utils(self, response, 200, 200, "注册成功")

    def test011_SMS_code_error(self):
        r = random.random()
        response = self.login_api.get_VerifyCode(self.session, str(r))
        self.assertEqual(200, response.status_code)

        response = self.login_api.get_sms_code(self.session, self.phone3, self.img_code, )
        logging.info("get_sms_code={}".format(response.json()))
        assert_utils(self, response, 200, 200, "短信发送成功")

        response = self.login_api.register(self.session, self.phone3, self.pwd)
        logging.info("register_success={}".format(response.json()))
        assert_utils(self, response, 200, 100, "验证码错误")

    def test012_img_code_error(self):
        r = random.random()
        response = self.login_api.get_VerifyCode(self.session, str(r))
        self.assertEqual(200, response.status_code)

        response = self.login_api.get_sms_code(self.session, self.phone3, self.img_code, )
        logging.info("get_sms_code={}".format(response.json()))
        assert_utils(self, response, 200, 200, "短信发送成功")

        response = self.login_api.register(self.session, self.phone3, self.pwd)
        logging.info("register_success={}".format(response.json()))
        assert_utils(self, response, 200, 100, "验证码错误")

    def test013_phone_number_exist(self):
        r = random.random()
        response = self.login_api.get_VerifyCode(self.session, str(r))
        self.assertEqual(200, response.status_code)

        response = self.login_api.get_sms_code(self.session, self.phone2, self.img_code, )
        logging.info("get_sms_code={}".format(response.json()))
        assert_utils(self, response, 200, 200, "短信发送成功")

        response = self.login_api.register(self.session, self.phone2, self.pwd)
        logging.info("register_success={}".format(response.json()))
        assert_utils(self, response, 200, 100, "手机已存在!")

    def test014_pwd_null(self):
        r = random.random()
        response = self.login_api.get_VerifyCode(self.session, str(r))
        self.assertEqual(200, response.status_code)

        response = self.login_api.get_sms_code(self.session, self.phone3, self.img_code, )
        logging.info("get_sms_code={}".format(response.json()))
        assert_utils(self, response, 200, 200, "短信发送成功")

        response = self.login_api.register(self.session, self.phone3, pwd="")
        logging.info("register_success={}".format(response.json()))
        assert_utils(self, response, 200, 100, "密码不能为空")

    def test015_disagree_clause(self):
        r = random.random()
        response = self.login_api.get_VerifyCode(self.session, str(r))
        self.assertEqual(200, response.status_code)

        response = self.login_api.get_sms_code(self.session, self.phone4, self.img_code, )
        logging.info("get_sms_code={}".format(response.json()))
        assert_utils(self, response, 200, 200, "短信发送成功")

        response = self.login_api.register(self.session, self.phone4, self.pwd)
        logging.info("register_success={}".format(response.json()))
        assert_utils(self, response, 200, 100, "请同意我们的条款")

    def test016_login_success(self):
        response = self.login_api.login_success(self.session, self.phone1, self.pwd)
        logging.info("login_success={}".format(response.json()))
        assert_utils(self, response, 200, 200, "登录成功")

    def test017_user_not_exist(self):
        response = self.login_api.login_success(self.session, "18366667891", self.pwd)
        logging.info("login_success={}".format(response.json()))
        assert_utils(self, response, 200, 100, "用户不存在")

    def test018_pwd_null(self):
        response = self.login_api.login_success(self.session, self.phone1, "")
        logging.info("login_success={}".format(response.json()))
        assert_utils(self, response, 200, 100, "密码不能为空")

    def test019_pwd_error(self):
        response = self.login_api.login_success(self.session, self.phone1, "error")
        logging.info("login_success={}".format(response.json()))
        assert_utils(self, response, 200, 100, "密码错误1次,达到3次将锁定账户")
        response = self.login_api.login_success(self.session, self.phone1, "123456")
        logging.info("login_success={}".format(response.json()))
        assert_utils(self, response, 200, 100, "密码错误2次,达到3次将锁定账户")
        response = self.login_api.login_success(self.session, self.phone1, "error")
        logging.info("login_success={}".format(response.json()))
        assert_utils(self, response, 200, 100, "由于连续输入错误密码达到上限，账号已被锁定，请于1.0分钟后重新登录")
        response = self.login_api.login_success(self.session, self.phone1, self.pwd)
        logging.info("login_success={}".format(response.json()))
        assert_utils(self, response, 200, 100, "由于连续输入错误密码达到上限，账号已被锁定，请于1.0分钟后重新登录")
        time.sleep(60)
        response = self.login_api.login_success(self.session, self.phone1, self.pwd)
        logging.info("login_success={}".format(response.json()))
        assert_utils(self, response, 200, 200, "登录成功")













