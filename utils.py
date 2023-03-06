import logging
import data
from itsdangerous import json

import app
import pymysql
import requests
from bs4 import BeautifulSoup


def assert_utils(self, response, status_code, status, desc):
    self.assertEqual(status_code, response.status_code)
    self.assertEqual(status, response.json().get("status"))
    self.assertIn(desc, response.json().get("description"))


def request_third_account(form_data):
    # 解析表单内容，并提取参数
    soup = BeautifulSoup(form_data, "html.parser")
    third_url = soup.form["action"]
    logging.info("third_url_response={}".format(third_url))
    data = {}
    for input in soup.find_all("input"):
        data.setdefault(input["name"], input["value"])
        logging.info("data={}".format(data))
    # 发送第三方请求

    response = requests.post(third_url, data=data)
    logging.info("third_url_response={}".format(response.text))
    return response

class DBuitls:
    @classmethod
    def get_conn(cls, db_name):
        conn = pymysql.connect(app.DB_URL, app.DB_USERNAME, app.DB_PASSWORD, db_name, autocommit=True)
        return conn

    @classmethod
    def close(cls, cursor=None, conn=None):
        if conn:
            conn.close()
        if cursor:
            cursor.close()

    @classmethod
    def delete(cls, db_name, sql):
        try:
            conn = cls.get_conn(db_name)
            cursor = conn.cursor()
            cursor.execute(sql)
        except Exception as e:
            conn.rollback()
        finally:
            cls.close(cursor, conn)


def read_imgVerify_data(file_name):
    file = app.BASE_DIR + "/data/" + file_name
    test_case_data = []
    with open(file, encoding="utf-8")as f:
        verify_data = json.load(f)
        test_data_list = verify_data.get("test_get_img_verify_code")
        for test_data in test_data_list:
            test_case_data .append((test_data.get("type"), test_data.get("status_code")))

    print("json_data={}".format(test_case_data))
    return test_case_data


def read_Smscode_data(file_name):
    file = app.BASE_DIR + "/data/" + file_name
    test_case_data = []
    with open(file, encoding="utf-8")as f:
        sms_data = json.load(f)
        test_data_list = sms_data.get("test_get_sms_code")
        for test_data in test_data_list:
            test_case_data.append((test_data.get("phone"), test_data.get("imgVerifyCode"), test_data.get("type"),
                                   test_data.get("status_code"), test_data.get("status"), test_data.get("description")))
    print("json_data={}".format(test_case_data))
    return test_case_data


def read_register_data(file_name):
    file = app.BASE_DIR + "/data/" + file_name
    test_case_data = []
    with open(file,encoding="utf-8")as f:
        register_data = json.load(f)
        test_data_list = register_data.get("test_register_data")
        for test_data in test_data_list:
            test_case_data.append((test_data.get("phone"), test_data.get("password"), test_data.get("imgVerifyCode"),
                                   test_data.get("phone_code"), test_data.get("dy_server"), test_data.get("invite_phone"),
                                   test_data.get("status_code"), test_data.get("status"), test_data.get("description")))
    print("json_data={}".format(test_case_data))
    return test_case_data


def read_param_data(filename, method_name, param_name):
    file = app.BASE_DIR + "/data/" + filename
    test_case_data = []
    with open(file, encoding="utf-8")as f:
        file_data = json.load(f)
        test_data_list = file_data.get(method_name)
        for test_data in test_data_list:
            test_params = []
            for params in param_name.split(","):
                test_params.append(test_data.get(params))
        test_case_data.append(test_params)
        print("test_params={}".format(test_case_data))
        return test_case_data

