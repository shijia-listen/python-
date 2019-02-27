# _*_ encoding:utf-8 _*_
import random
def code():
    code_y=''
    for i in range(4):
        num=random.randint(0,9)
        ret=chr(random.randint(65,122))
        a=str(random.choice([num,ret]))
        code_y=code_y+a
    return code_y
yan=code()
print(yan)

while True:
    code_a=input('请输入您的验证码:')
    if yan==code_a:
        print'输入验证码成功'
        break
    else:
        continue




