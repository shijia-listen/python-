a=input('plz input a:')
if ((a//10000)>1):
    print('a是由五位构成')
elif((a//1000)>1):
    print('a是由四位构成')
elif((a//100)>1):
    print('a是由三位构成')
elif((a//10)>1):
    print('a是由两位构成')
else:
    print 'a是由个位构成'

