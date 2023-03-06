# 导包
# 创建类
# 定义方法

import app
import requests


class LoginApi:
    def __init__(self):
        self.get_VerifyCode_url = app.BASE_URL+"/common/public/verifycode1/"
        self.get_sms_code_url = app.BASE_URL + "/member/public/sendSms"
        self.register_url = app.BASE_URL + "/member/public/reg"
        self.login_url = app.BASE_URL + "/member/public/login"

    def get_VerifyCode(self, session, r):
        url = self.get_VerifyCode_url + r
        response = session.get(url)
        return response

    def get_sms_code(self, session, phone, imgVerifyCode,type):
        data = {"phone": phone, "imgVerifyCode": imgVerifyCode, "type": type}

        response = session.post(self.get_sms_code_url, data=data)
        return response

    def register(self, session, phone, pwd, imgVerifyCode="8888", phoneCode="666666", dyServer="off",
                 invitephone=""):
        data={"phone": phone,
              "password": pwd,
              "verifycode": imgVerifyCode,
              "phone_code": phoneCode,
              "dy_server": dyServer,
              "invite_phone": invitephone}
        response = session.post(self.register_url, data=data)
        return response

    def login_success(self, session, keywords, paw):
        data = {"keywords": keywords,
                "password": paw}

        response = session.post(self.login_url, data=data)
        return response

