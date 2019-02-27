import random
while 1:
    s=int(random.randint(1,2))
    if s == 1:
        hand="手心"
    elif s == 2:
        hand == "手背"
    m=raw_input('输入 手心、手背, 输入"end"结束游戏：')
    alist=['手心','手背']
    if (m not in alist)and(m!='end'):
        print '输入错误,请重新输入!'
    elif(m not in alist)and(m=='end'):
        print '\n游戏退出中...'
        break
    elif m==hand:
        print  "电脑出了: "+hand+",平局!"
    elif (m=='手心' and hand=='手背'):
        print "电脑出了: "+hand+",你输了!"
    elif(m=='手背'and hand=='手心'):
         print "电脑出了: "+hand+",你赢了!"
    
