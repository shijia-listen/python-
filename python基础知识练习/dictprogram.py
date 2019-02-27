dictionary={}
addc='a'
while addc=='a'or 'c':
    addc=raw_input('添加或查找单词：(a/c)')
    if addc=='a':
        word=raw_input('输入单词(key):')
        defination=raw_input('输入定义值(value):')
        dictionary[str(word)]=str(defination)
        print '添加成功'
        print dictionary
    elif addc=='c':
        check_word=raw_input('要查找的单词：')
        for key in sorted(dictionary.keys()):
            if str(check_word)==key:
                print '该单词存在！',key,dictionary[key]
            else:
                print '该单词不存在！'
    else:
        print 'error type'
