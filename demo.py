# 先写一个没有封装的伪代码
# 导包
import requests

# 发送ihrm登录接口的请求
response = requests.post(url="http://ihrm-test.itheima.net/api/sys/login",
                         json={"mobile": "13800000002", "password": "123456"},
                         headers={"Content-Type": "Application/json"})
# 打印登录返回的数据
print("返回的数据为: ", response.json())
