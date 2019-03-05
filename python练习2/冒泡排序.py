li=[10,2,3,5,110,55,99,88,66]
def bubble_sort(li):
    count=len(li)
    for i in range(0,count):
        for j in range(i+1,count):
            if li[i]>li[j]:
                li[i],li[j]=li[j],li[i]
    return li
print(bubble_sort(li))
