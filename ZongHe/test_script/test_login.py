'''
登录
'''
import pytest
from ZongHe.caw import DataRead
from ZongHe.baw import Member
@pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/login_fail.yaml"))
def fail_data1(request):
    return request.param
# 登录失败
def test_login_fail(fail_data1,url,baserequests):
    # 发送请求
    r = Member.login(url,baserequests,fail_data1['casedata'])
    # 检查结果
    assert str(r.josn()['msg']) == str(fail_data1['expect']['msg'])
    assert str(r.josn()['code']) == str(fail_data1['expect']['code'])

