import getpass
n=0

while n <3:
    name = raw_input('�����������û���: ')
    pwd = getpass.getpass('��������������: ')
    if name=='listen' and pwd=='admin123':
        print('��ӭ�ɹ�����,listen')
        break
    else:
        print('�û������������!')
    n+=1   
       
            
