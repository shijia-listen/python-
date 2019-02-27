import time
ticks=time.time()
print '当前时间戳为：',ticks
print'---------------------------'
localtime=time.localtime(time.time())
print '本地时间为：',localtime
print '------------------------------------'
localtime=time.asctime(time.localtime(time.time()))
print '当地现在时间为：',localtime  #可读的时间
print '==========================================='
print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()) #格式化为2018-6-24 16:54:23
print '----------------------------------------------'
t=(2018,6,24,17,6,45,6,175,0)
secs=time.mktime(t)
print time.mktime(t)
print time.asctime(time.localtime(secs))
import calendar
cal=calendar.month(2018,10)
print '请输出2018年10月的日历：'
print cal
