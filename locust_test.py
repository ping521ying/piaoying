'''
性能测试
'''
from locust import HttpUser,between,task
from locust import LoadTestShape
import math
'''
1.为要模拟的用户定义一个类，从HttpUser继承
'''
class CarRental(HttpUser):
    # between 是User类中定义的一个方法
    # wait_time是User类定义的一个属性，表示等待时间
    wait_time = between(3,8) # 任务跟任务之间的等待时间在3~8之间取值机数
    @task
    def carMangage(self):
        self.client.get("/carRental/rent/loadAllRent.action?page=1&limit=10")
    @task
    def loadAkkMenu(self):
        self.client.get("/carRental/menu/loadAllMenu.action?page=1&limit=10")
# -f 要执行的文件
# -- host 被测系统
# --web-host locut web 页面的访问地址
# -- web-port locut web 页面的访问端口
# locust -f locust_test.py --host=http://127.0.0.1:8089 --web-host=127.0.0.1 --web-poet=8088
# locust -f locust_test.py --step-load
# class StepLoadShape(LoadTestShape):
#     """
#     A step load shape
#
#
#     Keyword arguments:
#
#         step_time -- Time between steps
#         step_load -- User increase amount at each step
#         spawn_rate -- Users to stop/start per second at every step
#         time_limit -- Time limit in seconds
#
#     """
#
#     step_time = 30
#     step_load = 10
#     spawn_rate = 10
#     time_limit = 600
#
#     def tick(self):
#         run_time = self.get_run_time()
#
#         if run_time > self.time_limit:
#             return None
#
#         current_step = math.floor(run_time / self.step_time) + 1
#         return (current_step * self.step_load, self.spawn_rate)
class DoubleWave(LoadTestShape):
    """
    A shape to immitate some specific user behaviour. In this example, midday
    and evening meal times.

    Settings:
        min_users -- minimum users
        peak_one_users -- users in first peak
        peak_two_users -- users in second peak
        time_limit -- total length of test
    """

    min_users = 20
    peak_one_users = 60
    peak_two_users = 40
    time_limit = 600

    def tick(self):
        run_time = round(self.get_run_time())

        if run_time < self.time_limit:
            user_count = (
                (self.peak_one_users - self.min_users)
                * math.e ** -(((run_time / (self.time_limit / 10 * 2 / 3)) - 5) ** 2)
                + (self.peak_two_users - self.min_users)
                * math.e ** -(((run_time / (self.time_limit / 10 * 2 / 3)) - 10) ** 2)
                + self.min_users
            )
            return (round(user_count), round(user_count))
        else:
            return None