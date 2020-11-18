import requests
url = "http://jy001:8888/futureloan/mvc/api/member/register"
canshu = {"mobilephone":"null","pwd":"123456abc","regname":"aaa"}
r = requests.post(url,data=canshu)
print(r.text)



