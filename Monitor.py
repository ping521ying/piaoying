'''
监控代码：监控服务器的内存，CPU，网络，磁盘等。与租车系统部署到一起
'''
import psutil
from datetime import datetime
from time import sleep

print(psutil.cpu_percent()) # 获取CPU信息
print(psutil.virtual_memory()) # 虚拟内存
print(psutil.virtual_memory().percent) # 虚拟内存百分比
print(psutil.disk_usage("c:/")) # 租车系统所在的磁盘
print(psutil.disk_usage("c:/").percent) # 租车系统所在的磁盘的百分比
print(psutil.net_io_counters()) # 网络
print(psutil.net_io_counters().bytes_sent) # 发送的字节数
print(psutil.net_io_counters().bytes_recv) # 接收的字节数

# 达到类似serveragent的效果，在性能测色期间，获取cpu，内存趋势
# 死循环，每隔3s读一次，把读的结果写到文件中，测试结束后分析文件，使用excel等生产图表。
# 时间戳 cpu% 内存% 磁盘% 发送字节数 接收字节数
with open("c:/资源占用情况.txt",encoding='utf-8',mode='a') as file:
    file.write("时间戳\t cpu%\t 内存%\t 磁盘% \t发送字节数\t 接收字节数")
    while True:
        print("监控中。。。。。。")
        file.write(datetime.strftime(datetime.now(),"%y-%m-%d %H:%M:%S")+"%\t")
        file.write(str(psutil.cpu_percent())+"%\t")
        file.write(str(psutil.virtual_memory())+"%\t")
        file.write(str(psutil.virtual_memory().percent)+"\t")
        file.write(str(psutil.disk_usage("c:/").percent)+"\t")
        file.write(str(psutil.net_io_counters().bytes_sent)+"\t")
        file.write(str(psutil.net_io_counters().bytes_recv)+"\n")
        file.flush()
        sleep(3)




