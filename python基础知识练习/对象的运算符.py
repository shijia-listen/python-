class Programer(object):
    def __new__(cls,*args,**kwargs):
        print 'call __new__method'
        print args
        return super(Programer,cls).__new__(cls,*args,**kwargs)
    def __init__(self,name,age):
        print 'call __init__method'
        self.name=name
        self.age=age
    def __add__(self,other):
        if isinstance(other,Programer):
            return self.age + other.age
        else:
            raise Excertion('The type of object must be Programer ')
    def __eq__(self,other):
        if isinstance(other,Programer):
            if self.age==other.age:
                print 'True'
            else:
                print 'False'
        else:
            raise Excertion('The type of object must be Programer ')
    def __str__(self):
        return '%s is %s years old'%(self.name,self.age)
    def __dir__(self):
        return self.__dir__.keys()
            
if __name__=='__main__':
    p1=Programer('Danny',15)
    p2=Programer('lilei',20)
    print p1==p2
    print p1+p2
