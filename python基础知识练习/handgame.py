import random
while 1:
    s=int(random.randint(1,2))
    if s == 1:
        hand="����"
    elif s == 2:
        hand == "�ֱ�"
    m=raw_input('���� ���ġ��ֱ�, ����"end"������Ϸ��')
    alist=['����','�ֱ�']
    if (m not in alist)and(m!='end'):
        print '�������,����������!'
    elif(m not in alist)and(m=='end'):
        print '\n��Ϸ�˳���...'
        break
    elif m==hand:
        print  "���Գ���: "+hand+",ƽ��!"
    elif (m=='����' and hand=='�ֱ�'):
        print "���Գ���: "+hand+",������!"
    elif(m=='�ֱ�'and hand=='����'):
         print "���Գ���: "+hand+",��Ӯ��!"
    
