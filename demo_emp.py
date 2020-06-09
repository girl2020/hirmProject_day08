# 用不封装的代码实现鱼员工模块的添加,查询,修改,删除
"""
1. 首先我们需要调用登录接口来实现irhm的登录
2. 打印返回的数据
3. 需要提取登录成功返回的令牌来作为添加员工, 查询员工, 修改员工, 删除员工的请参参数
4. 添加成功员工后需要打印返回的数据
5. 提取返回员工id作为查询员工, 修改员工, 删除员工的url中的参数部分
"""
# 导包
import requests

# 发送ihrm登录接口的请求
response = requests.post(url="http://ihrm-test.itheima.net/api/sys/login",
                         json={"mobile": "13800000002", "password": "123456"},
                         headers={"Content-Type": "Application/json"})
# 打印登录返回的数据
print("返回的数据为: ", response.json())

# 提取返回的令牌
token = "Bearer " + response.json().get("data")
# 打印提取的令牌
print("获取的令牌为: ", token)
# 调用添加员工的接口
headers = {"Content-Type": "Application/json", "Authorization": token}

response_emp = requests.post(url="http://ihrm-test.itheima.net" + "/api/sys/user",
                             json={"username": "糖糖112346丫丫呀52021",
                                   "mobile": "18933231399",
                                   "timeOfEntry": "2020-05-05",
                                   "formOfEmployment": 1,
                                   "departmentName": "测试部",
                                   "departmentId": "1063678149528784896",
                                   "correctionTime": "2020-05-30T16:00:00.000Z"
                                   },
                             headers=headers)
# 打印添加员工返回的数据
print("添加员工的结果为: ", response_emp.json())
# 提取返回的数据中的员工id
emp_id = response_emp.json().get("data").get("id")
# # 打印提取的id
print("员工id为: ", emp_id)
# 调用查询员工的接口
select_url = "http://ihrm-test.itheima.net" + "/api/sys/user" + "/" + emp_id
response_select = requests.get(url=select_url, headers=headers)
# 打印查询返回的结果
print("查询员工的结果为: ", response_select.json())
# 调用修改员工的接口
modify_url = "http://ihrm-test.itheima.net" + "/api/sys/user" + "/" + emp_id
response_modify = requests.put(url=modify_url, json={"username": "糖糖1234哈哈哈哈呀"},
                               headers=headers)
# 打修改员工名称的结果
print("修改后的结果为： ", response_modify.json())
# 调用删除员工的接口
delete_url = "http://ihrm-test.itheima.net" + "/api/sys/user" + "/" + emp_id
response_delete = requests.delete(url=delete_url, headers=headers)
# 打印删除员工的结果
print("删除员工的结果为: ", response_delete.json())
