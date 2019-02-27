#num=int(raw_input('plz input your number:'))
#print (num*'*')
#for i in range(num-2):
    #print '*'+' '*(num-2)+'*'
#print (num*'*')
n=input('plz input your number:')
i=0
while(i<n):
    i+=1
    if i==1 or i==n:
        print '* '*n
    
    else:
        print '*'+' '*(n+1)+'*'
