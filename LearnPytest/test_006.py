'''
mark标记
1.skip:这个版本有缺陷，导致某个用列执行不通过，可以跳过这个用列的执行，
2.自定义标记,
  随着代码规模增加，包含功能测试，接口测试，性能测试，冒烟测试，执行
'''
import pytest
def test_case1():
    print("测试用列1")
@pytest.mark.skip(reason="有缺陷，缺陷号为23423408234，待缺陷解决后再执行")
def test_case2():
    print("测试用列2")
@ pytest.mark.maoyan
def test_case3():
    print("测试用列3")

@pytest.mark.api
class TestUserMark:
    @pytest.mark.maoyan
    def test_case4(self):
        print("测试用列4")
    def test_case5(self):
        print("测试用列5")
    def test_case6(self):
        print("测试用列6")