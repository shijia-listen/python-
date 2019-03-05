def select_sort(l):
    min_num=0
    for i in range(len(l)-1):
        min_num=i
        for j in range(i+1,len(l)):
            if l[min_num]>l[j]:
                min_num=j
        l[min_num],l[i]=l[i],l[min_num]
    return l
l=[1,4,2,3,9,5,7,6,8,10]
print(select_sort(l))
