import time
ticks=time.time()
print '��ǰʱ���Ϊ��',ticks
print'---------------------------'
localtime=time.localtime(time.time())
print '����ʱ��Ϊ��',localtime
print '------------------------------------'
localtime=time.asctime(time.localtime(time.time()))
print '��������ʱ��Ϊ��',localtime  #�ɶ���ʱ��
print '==========================================='
print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()) #��ʽ��Ϊ2018-6-24 16:54:23
print '----------------------------------------------'
t=(2018,6,24,17,6,45,6,175,0)
secs=time.mktime(t)
print time.mktime(t)
print time.asctime(time.localtime(secs))
import calendar
cal=calendar.month(2018,10)
print '�����2018��10�µ�������'
print cal
