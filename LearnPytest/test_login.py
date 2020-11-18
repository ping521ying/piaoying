import pytest,requests,json
@pytest.fixture(params=[{"casedata":{"mobilephone":"137123456789","pwd":"123456abc","regname":"aaa"},
                        "expect":{"status":"0","code":"20109","msg":"手机号码格式不正确"}},
                        {"casedata":{"mobilephone":"null","pwd":"123456abc","regname":"aaa"},
                        "expect":{"status":"0","code":"20109","msg":"参数不能为空"}},
                        {"casedata":{"mobilephone":"13745241111","pwd":"123456abc","regname":"aaa"},
                        "expect":{"status":"0","code":"20110","msg":"手机号码已被注册"}}])
def data2(request):
    return request.param
def test_login4(data2):
    print(f"使用手机号码{data2['casedata']}测试注册功能,预期结果为{data2['expect']}")
def register1(data3):
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    r = requests.post(url,data=data3)
    return r
def test_register1(data2):
    real = register1(data2['casedata'])
    assert real.json()['msg'] == data2['expect']['msg']
    assert real.json()['code'] == data2['expect']['code']

