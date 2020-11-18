'''
注册的测试脚本（pytest）
'''
import pytest
from ZongHe.caw import DataRead
from ZongHe.baw import Member,DbOp

# 测试前置：获取测试数据，数据是列表，通过readyaml读取来的
@pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/register_fial.yaml"))
def fail_data(request):
    return request.param

# 注册失败
def test_register_fail(fail_data,url,baserequests):
    print(f"测试数据为:{fail_data['casedata']}")
    print(f"预期结果为:{fail_data['expect']}")
    # 发送请求
    r = Member.login(url,baserequests,fail_data['casedata'])
    print(r.text)
    # 检查结果
    assert str(r.json()['msg'])==str(fail_data['expect']['msg'])
    assert str(r.json()['status']) == str(fail_data['expect']['status'])
    assert str(r.json()['code']) == str(fail_data['expect']['code'])
# 测试前置：获取测试数据，数据是列表，通过readyaml读取来的
@pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/register_pass"))
def pass_data(request):
    return request.param
# 注册成功
def test_register_pass(pass_data,baserequests,url,db):
    print(f"测试数据为:{pass_data['casedata']}")
    print(f"预期结果为:{pass_data['expect']}")
    phone = pass_data['casedata']['mobilephone']
    # 初始化，确保环境中没有影响本次执行的数据
    DbOp.deleteUser(db,phone)
    # 发送请求
    r = Member.register(url, baserequests, pass_data['casedata'])
    print(r.text)
    # 1. 检查响应结果
    assert str(r.json()['msg']) == str(pass_data['expect']['msg'])
    assert str(r.json()['status']) == str(pass_data['expect']['status'])
    assert str(r.json()['code']) == str(pass_data['expect']['code'])
    # 2.检查实际有没有注册成功（1.查数据库;2.获取用户列表；3.用注册）
    r = Member.getlist(url,baserequests)
    assert phone in r.text
    # 清理环境，根据手机删除注册用户
    DbOp.deleteUser(db, phone)
# 重复注册
def test_register_repeat():
    pass

