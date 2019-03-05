def funzip(c):
    list1=list(c)
    list2=list1[:]
    i=0
    j=2
    a=0
    temp=""
    for x in list1:
        i+=1
        a+=1
        print(i)
        if a<len(list1):
            if list2[i]==temp and j>2:
                j+=1
                list2.pop(i)
                list2[i-1]=str(j-1)
                i-=1
            elif list2[i]==list2[i-1] and j==2:
                list2[i]=str(j)
                temp=list2[i-1]
                j+=1
            elif list2[i]!=temp and j>2:
                temp=""
                j=2
        return("".join(list2))
c='aaabbbbccd'
print(funzip(c))
            
