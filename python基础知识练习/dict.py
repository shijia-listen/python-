seq=('hello','world','ni','hao')  #Ԫ��
dict=dict.fromkeys(seq)
print dict  #������ֵ����һ���ֵ�
dict=dict.fromkeys(seq,10)
print dict   #�趨��һ����ֵ��������һ����value���ֵ䡣
print '-----------'
dict={'name':'tom','sex':'male','age':10,'habbit':'basketball'}
print dict.get('name')  #�ֵ��������ֵ�ͷ���������Ӧ��ֵ
print dict.get('hair')  #û�����������Ӧ��ֵ�����û�и���default���ͷ���none�����򷵻�default
print '--------------------'
print dict.has_key('sex')
print dict.has_key('hair')#���ֵ���Ҫ���ҵļ��Ƿ����ֵ��У��ڷ���ture�����򷵻�false��
print '--------------------'
print dict.items()  #���б����ʽ����Ԫ������
for key,value in dict.items():
    print key,value  #ͨ��ѭ���ɱ���������ֵ��Ԫ������
print '------------------------'
print dict.keys()
# ���б���ʽ�����ֵ������еļ���
print dict.setdefault('name')
print dict.setdefault('haircolor','red')  #��get()��������
dict2={'hair':'red','address':'beijing'}
dict.update(dict2) #���ֵ�2�еļ�ֵ���µ��ֵ�1��
print dict
print dict.values() #����ֵ������е�ֵ
print dict.pop('hair')  #ɾ��������Ӧ��ֵ�����ر�ɾ����ֵ��key�������\
print dict
print '--------------------------------------------------------'
print dict.popitem()
print dict  #������ز�ɾ���ֵ���һ�Լ���ֵ


