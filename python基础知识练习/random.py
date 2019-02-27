
#验证码的生成
import random
def code():
    code_y=''
    for i in range(4):
        num=random.randint(0,9)
        ret=chr(random.randint(65,122))
        a=str(random.choice([num,ret]))
        code_y+=a
    return code_y
print(code())
        
   
