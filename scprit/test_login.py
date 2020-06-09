# 定义irhm登录测试类

# 导包
import logging
import unittest

from parameterized import parameterized

import app
from api.login_api import LoginApi
from demo import response
from utils import assert_common, read_login_data


# 定义irhm登录测试类
class TestLogin(unittest.TestCase):
    # 定义类的初始化fixture
    @classmethod
    def setUpClass(cls):
        # 实例化封装的登录接口
        cls.login_api = LoginApi()

    # 定义类的销毁fixture
    @classmethod
    def tearDownClass(cls):
        pass

    # 定义登录登录数据文件的路径
    file_path = app.BASE_DIR + "/data/login.json"

    # 实现登录参数化
    @parameterized.expand(read_login_data(file_path))
    # 定义测试登录的测试用例方法
    # 定义登录成功测试用例
    # def test01_login_success(self):
    #     # 调用封装好的登录接口中获取登录接口的方法,并返回登录结果
    #     response = self.login_api.login(json={"mobile": "13800000002", "password": "123456"},
    #                                     headers={"Content-Type": "Application/json"})
    #     # 用logging打印返回的结果数据
    #     logging.info("登录成功的结果为: {}" .format(response.json()))
    #     # 断言
    #     # self.assertEqual(200, response.status_code)
    #     # self.assertEqual("True", response.json().get("success"))
    #     # self.assertEqual(10000, response.json().get("code"))
    #     # self.assertEqual("操作成功", response.json().get("message"))
    #
    #     # 调用utils中定义的通用断言函数
    #     assert_common(self, 200, True, 10000, "操作成功", response)
    #
    # # 定义手机号码为空(bug)
    # def test02_mobile_is_empty(self):
    #     # 调用封装好的登录接口中获取登录接口的方法,并返回登录结果
    #     response = self.login_api.login(json={"mobile": "", "password": "error"},
    #                                     headers={"Content-Type": "Application/json"})
    #     # 用logging打印返回的结果数据
    #     logging.info("手机号码为空的结果为: {}".format(response.json()))
    #     # 调用utils中定义的通用断言函数
    #     assert_common(self, 200, False, 20001, "用户名或密码错误", response)
    #
    # # 定义手机号码不存在
    # def test03_mobile_not_exist(self):
    #     # 调用封装好的登录接口中获取登录接口的方法,并返回登录结果
    #     response = self.login_api.login(json={"mobile": "17564324673", "password": "123456"},
    #                                     headers={"Content-Type": "Application/json"})
    #     # 用logging打印返回的结果数据
    #     logging.info("手机号码不存在的结果为: {}".format(response.json()))
    #     # 调用utils中定义的通用断言函数
    #     assert_common(self, 200, False, 20001, "用户名或密码错误", response)
    #
    # # 密码错误
    # def test04_error_password(self):
    #     # 调用封装好的登录接口中获取登录接口的方法,并返回登录结果
    #     response = self.login_api.login(json={"mobile": "13800000002", "password": "1234567"},
    #                                     headers={"Content-Type": "Application/json"})
    #     # 用logging打印返回的结果数据
    #     logging.info("密码错误的结果为: {}".format(response.json()))
    #     # 调用utils中定义的通用断言函数
    #     assert_common(self, 200, False, 20001, "用户名或密码错误", response)
    #
    # # 密码为空
    # def test04_password_is_empty(self):
    #     # 调用封装好的登录接口中获取登录接口的方法,并返回登录结果
    #     response = self.login_api.login(json={"mobile": "13800000002", "password": ""},
    #                                     headers={"Content-Type": "Application/json"})
    #     # 用logging打印返回的结果数据
    #     logging.info("密码为空的结果为: {}".format(response.json()))
    #     # 调用utils中定义的通用断言函数
    #     assert_common(self, 200, False, 20001, "用户名或密码错误", response)
    #
    # # 无参
    # def test05_parameter_is_none(self):
    #     # 调用封装好的登录接口中获取登录接口的方法,并返回登录结果
    #     response = self.login_api.login(json={},
    #                                     headers={"Content-Type": "Application/json"})
    #     # 用logging打印返回的结果数据
    #     logging.info("无参的结果为: {}".format(response.json()))
    #     # 调用utils中定义的通用断言函数
    #     assert_common(self, 200, False, 20001, "用户名或密码错误", response)
    #
    # # 传入null
    # def test06_null(self):
    #     # 调用封装好的登录接口中获取登录接口的方法,并返回登录结果
    #     response = self.login_api.login(None,
    #                                     headers={"Content-Type": "Application/json"})
    #     # 用logging打印返回的结果数据
    #     logging.info("传入None的结果为: {}".format(response.json()))
    #     # 调用utils中定义的通用断言函数
    #     assert_common(self, 200, False, 99999, "抱歉，系统繁忙，请稍后重试！", response)
    #
    # # 多参
    # def test07_more_param(self):
    #     # 调用封装好的登录接口中获取登录接口的方法,并返回登录结果
    #     response = self.login_api.login(json={"mobile": "13800000002", "password": "123456", "extras_params":"1"},
    #                                     headers={"Content-Type": "Application/json"})
    #     # 用logging打印返回的结果数据
    #     logging.info("传入多参的结果为: {}".format(response.json()))
    #     # 调用utils中定义的通用断言函数
    #     assert_common(self, 200, True, 10000, "操作成功", response)
    #
    # # 少参 - 缺少mobile
    # def test08_less_param_mobile(self):
    #     # 调用封装好的登录接口中获取登录接口的方法,并返回登录结果
    #     response = self.login_api.login(json={"password": "123456"},
    #                                     headers={"Content-Type": "Application/json"})
    #     # 用logging打印返回的结果数据
    #     logging.info("缺少mobile的结果为: {}".format(response.json()))
    #     # 调用utils中定义的通用断言函数
    #     assert_common(self, 200, False, 20001, "用户名或密码错误", response)
    #
    # # 少参 - 缺少password
    # def test08_less_param_password(self):
    #     # 调用封装好的登录接口中获取登录接口的方法,并返回登录结果
    #     response = self.login_api.login(json={"mobile": "13800000002"},
    #                                     headers={"Content-Type": "Application/json"})
    #     # 用logging打印返回的结果数据
    #     logging.info("缺少password的结果为: {}".format(response.json()))
    #     # 调用utils中定义的通用断言函数
    #     assert_common(self, 200, False, 20001, "用户名或密码错误", response)
    #
    # # 错误参数
    # def test09_error_param(self):
    #     # 调用封装好的登录接口中获取登录接口的方法,并返回登录结果
    #     response = self.login_api.login(json={"molibe": "13800000002", "password": "123456"},
    #                                     headers={"Content-Type": "Application/json"})
    #     # 用logging打印返回的结果数据
    #     logging.info("错误参数的结果为: {}".format(response.json()))
    #     # 调用utils中定义的通用断言函数
    #     assert_common(self, 200, False, 20001, "用户名或密码错误", response)
    def test01_login(self, case_name, request_body, success, code, message, http_code):
        # 使用封装的登录接口发送请求
        response = self.login_api.login(request_body, {"Content-Type": "application/json"})
        # 打印响应数据
        logging.info("登录的结果为：{}".format(response.json()))
        # 断言
        assert_common(self, http_code, success, code, message, response)

