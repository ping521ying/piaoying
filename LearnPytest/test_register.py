'''
pytest命名规则：
1.测试文件以test_开头或结尾
2.测试类以test开头
3.测试方法、函数以test_开头
'''
import requests
import json

def register(data):
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    r = requests.post(url,data=data)
    return r

# 手机号码格式不正确
def test_register_001():
    # 测试数据
    data = {"mobilephone":"1801234567","pwd":"123456abc","regname":"aaa"}
    # 预期结果
    expect = {"status":"0","code":"20109","msg":"手机号码格式不正确"}
    print(json.dumps(expect))
    # 测试步骤
    real = register(data) # 字典转json
    # 检查结果
    assert real.json()['msg'] == expect['msg']
    assert real.json()['code'] == expect['code']

# 手机号码不能为空
def test_register_002():
    # 测试数据
    data = {"mobilephone": "null", "pwd": "123456abc", "regname": "aaa"}
    # 预期结果
    expect = {"status": "0", "code": "20109", "msg": "手机号码不能为空"}
    print(json.dumps(expect))
    # 测试步骤
    real = register(data) # 字典转json
    # 检查结果
    assert real.json()['msg'] == expect['msg']
    assert real.json()['code'] == expect['code']
# 手机号码已被注册
def test_register_003():
    # 测试数据
    data = {"mobilephone": "18012345678", "pwd": "123456abc", "regname": "aaa"}
    # 预期结果
    expect = {"status": "0", "code": "20110", "msg": "手机号码已被注册"}
    print(json.dumps(expect))
    # 测试步骤
    real = register(data) # 字典转json
    # 检查结果
    assert real.json()['msg'] == expect['msg']
    assert real.json()['code'] == expect['code']
















































































































































































































































































































