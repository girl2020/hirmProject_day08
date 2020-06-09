# 导包
import logging
import unittest

from parameterized import parameterized

import app
from api.employee import EmployeeApi

from api.login_api import LoginApi
from demo import response
from utils import assert_common, read_emp_data


# 定义测试类
class TestEmployee(unittest.TestCase):
    # 定义初始化fixture
    def setUp(self):
        # 实例化封装的登录接口
        self.login_api = LoginApi()
        # 实例化封装的员工接口
        self.emp_api = EmployeeApi()

    def tearDown(self):
        pass

    # 实现登录成功的接口
    def test01_login_success(self):
        # 调用封装好的登录的接口发送登录接口请求
        response_login = self.login_api.login({"mobile": "13800000002", "password": "123456"},
                                              {"Content-Type": "Application/json"})

        # 打印登录结果
        logging.info("返回的结果为: {}".format(response_login.json()))
        # 提取登录后的令牌
        token = "Bearer " + response_login.json().get("data")
        # 把令牌拼接成HEADERS并保存到全局变量HEADERS
        app.HEADERS = {"Content-Type": "application/json", "Authorization": token}
        # 打印请求头
        logging.info("保存到全局变量的请求头为: {}".format(app.HEADERS))
        # 断言
        assert_common(self, 200, True, 10000, "操作成功", response)

    # 定义员工模块的文件路径
    file_path = app.BASE_DIR + "/data/emp.json"

    # 实现添加员工的接口
    # 参数化
    @parameterized.expand(read_emp_data(file_path, 'add_emp'))
    def test02_add_emp(self, username, mobile, success, code, message, http_code):
        # 调用封装好的员工的接口发送添加员工接口请求
        response_add = self.emp_api.add_emp(username, mobile, app.HEADERS)
        # 打印添加员工的结果
        logging.info("添加员工的结果为: {}".format(response_add.json()))
        # 提取添加员工中的id保存到全局变量中
        app.EMP_ID = response_add.json().get("data").get("id")
        # 打印保存导全局变量中的id
        logging.info("保存到全局变量中的id为: {}".format(app.EMP_ID))
        # 断言
        assert_common(self, http_code, success, code, message, response)

    # 实现查询员工的接口
    # 参数化
    @parameterized.expand(read_emp_data(file_path, 'select_emp'))
    def test03_select_emp(self, success, code, message, http_code):
        # 调用封装好的员工的接口发送查询员工接口请求
        response_select = self.emp_api.select_emp(app.EMP_ID, app.HEADERS)
        # 打印查询员工的结果
        logging.info("查询员工的结果为: {}".format(response_select.json()))
        # 断言
        assert_common(self, http_code, success, code, message, response)

    # 实现修改员工的接口
    # 参数化
    @parameterized.expand(read_emp_data(file_path, 'modify_emp'))
    def test04_modify_emp(self, username, success, code, message, http_code):
        # 调用封装好的员工的接口发送修改员工接口请求
        response_modify = self.emp_api.modify_emp(username, app.EMP_ID, app.HEADERS)
        # 打印修改员工的结果
        logging.info("修改员工的结果为: {}".format(response_modify.json()))
        # 断言
        assert_common(self, http_code, success, code, message, response)

    # 实现删除员工的接口
    # 参数化
    @parameterized.expand(read_emp_data(file_path, 'delete_emp'))
    def test05_delete_emp(self,success, code, message, http_code):
        # 调用封装好的员工的接口发送删除员工接口请求
        delete_modify = self.emp_api.delete_emp(app.EMP_ID, app.HEADERS)
        # 打印删除员工的结果
        logging.info("删除员工的结果为: {}".format(delete_modify.json()))
        # 断言
        assert_common(self, http_code, success, code, message, response)
