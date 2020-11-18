'''
测试登录功能
'''
import pytest
from ZongHe.caw import DataRead
from ZongHe.baw import DbOp,Member

@pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/login_data.yaml"))
def login_data(request):
    return request.param
@pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/login_setup.yaml"))
def setup_data(request):
    return request.param
# 测试前置和后置
@pytest.fixture()
def register(setup_data,url,baserequests,db):
    # 注册
    phone = setup_data['casedata']['mobilephone']
    DbOp.deleteUser(db,phone)
    yield
    # 删除注册用户
    DbOp.deleteUser(db,phone)
def test_login(register,login_data,url,baserequests):
    # 登录
    # 检查登录的结果
    r = Member.login(url,baserequests,login_data['casedata'])
    assert r.json()['msg'] == login_data['expect']['msg']