import requests
from unittest import mock

class Register:
    def register1(self,data):
        url = "http://jy001:8081/futureloan/mvc/api/member/register"
        r = requests.post(url,data=data).json()
        return r
class Test_Register2:
    register = Register()
    register.register1 = mock.Mock(return_value={"status":"0","code":"20103","msg":"参数不能为空"})
    data = {"mobilephone":"null","pwd":"123456abc","regname":"aaa"}
    r = register.register1(data)
    print(r)
   assert r['msg'] == "参数不能为空"