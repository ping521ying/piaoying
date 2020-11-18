'''
脚本层的公共方法
'''
import pytest
from ZongHe.caw import DataRead
from ZongHe.caw.BaseRequests import BaseRequests
# 从环境文件中读取url
@pytest.fixture(scope='session')
def url():
    return  DataRead.readini("ZongHe/data_env/env.ini","url")
# 从环境文件中读取db
@pytest.fixture(scope='session')
def db():
    return eval( DataRead.readini("ZongHe/data_env/env.ini","db"))
@pytest.fixture(scope='session')
def baserequests():
    return BaseRequests()