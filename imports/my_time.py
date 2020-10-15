import time
import datetime as dt
print(time.time())
# 获取当时时间戳 1601995944.292 小数点之前是秒

time.sleep(3)  # 程序在此停留三秒
# 时间戳是从:
#   UTC时间 1970-01-01 00:00:00  到现在-8小时的秒数
#   北京时间 1970-01-01 08:00:00  到现在的秒数
# 北京时间是东八区是UTC+8 不是 UTC时间

print(time.strftime("%Y/%m-%d %H:%M:%S"))  #按指定格式输出时间
print(time.asctime())  #按指定格式输出时间


#===============dt====================
print(dt.datetime.now())   #获取当前时间
print(dt.date(2020, 10, 12)) #生成日期
print(dt.time(20, 35, 00))  #生成时间
print(dt.datetime.now() + dt.timedelta(3)) #获取三天后的时间