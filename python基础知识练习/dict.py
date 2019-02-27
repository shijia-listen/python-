seq=('hello','world','ni','hao')  #元组
dict=dict.fromkeys(seq)
print dict  #根据列值创建一个字典
dict=dict.fromkeys(seq,10)
print dict   #设定了一个键值，生成了一个带value的字典。
print '-----------'
dict={'name':'tom','sex':'male','age':10,'habbit':'basketball'}
print dict.get('name')  #字典中有这个值就返回列所对应的值
print dict.get('hair')  #没有这个列所对应的值，如果没有给定default，就返回none，否则返回default
print '--------------------'
print dict.has_key('sex')
print dict.has_key('hair')#看字典中要查找的键是否在字典中，在返回ture，否则返回false。
print '--------------------'
print dict.items()  #以列表的形式返回元组数组
for key,value in dict.items():
    print key,value  #通过循环可遍历（键，值）元祖数组
print '------------------------'
print dict.keys()
# 以列表形式返回字典中所有的键。
print dict.setdefault('name')
print dict.setdefault('haircolor','red')  #和get()方法相似
dict2={'hair':'red','address':'beijing'}
dict.update(dict2) #把字典2中的键值更新到字典1中
print dict
print dict.values() #输出字典中所有的值
print dict.pop('hair')  #删除键所对应的值，返回被删除的值，key必须给出\
print dict
print '--------------------------------------------------------'
print dict.popitem()
print dict  #随机返回并删除字典中一对键和值


