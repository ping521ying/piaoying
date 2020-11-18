'''
数据库操作
1.数据库从mysql换成sqlite,脚本层不用改动caw里面的mysqlop.py
'''
from ZongHe.caw import MySqlOp
def deleteUser(db,phone):
    '''
    根据手机号删除用户
    :param db: 一个字典，存储数据库信息
    :param phone: 手机号
    :return:
    '''
    conn = MySqlOp.connect(db)
    MySqlOp.execute(conn,f'delete from Member where MobilePhone = 18012345678;')
    MySqlOp.disconnect(conn)