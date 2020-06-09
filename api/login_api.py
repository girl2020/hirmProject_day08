# 导包
import requests


# 封装irhm登录接口
class LoginApi:
    def __init__(self):
        # 初始化登录的url
        self.login_url = "http://ihrm-test.itheima.net" + "/api/sys/login"

    # 定义获取irhm登录接口的方法
    def login(self, json, headers):
        # 发送登录接口的请求
        return requests.post(url=self.login_url, json=json, headers=headers)
