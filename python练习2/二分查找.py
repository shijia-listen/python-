def binary_select(l,num):
    if 1:
        mid=len(l)//2
        if num > l[mid]:
            binary_select(l[mid+1:],num)
        elif num < l[mid]:
            binary_select(l[:mid],num)
        elif num == l[mid]:
            print('此数在列表中')
    else:
        print('此数不在列表中')
l=[1,2,3,4,5,10,33,88]
binary_select(l,100)
        
        
            
             
        
