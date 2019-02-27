import getpass
n=0

while n <3:
    name = raw_input('请输入您的用户名: ')
    pwd = getpass.getpass('请输入您的密码: ')
    if name=='listen' and pwd=='admin123':
        print('欢迎成功登入,listen')
        break
    else:
        print('用户名或密码错误!')
    n+=1   
       
            
