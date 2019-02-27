class Programer(object):
    def __new__(cls,*args,**kwargs):
        print 'call __new__method'
        print args
        return super(Programer,cls).__new__(cls,*args,**kwargs)
    def __init__(self,name,age):
        print 'call __init__method'
        self.name=name
        self.age=age
if __name__=='__main__':
    programer=Programer('Danny',15)
    print programer.__dict__
