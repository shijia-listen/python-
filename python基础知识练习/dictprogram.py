dictionary={}
addc='a'
while addc=='a'or 'c':
    addc=raw_input('��ӻ���ҵ��ʣ�(a/c)')
    if addc=='a':
        word=raw_input('���뵥��(key):')
        defination=raw_input('���붨��ֵ(value):')
        dictionary[str(word)]=str(defination)
        print '��ӳɹ�'
        print dictionary
    elif addc=='c':
        check_word=raw_input('Ҫ���ҵĵ��ʣ�')
        for key in sorted(dictionary.keys()):
            if str(check_word)==key:
                print '�õ��ʴ��ڣ�',key,dictionary[key]
            else:
                print '�õ��ʲ����ڣ�'
    else:
        print 'error type'
