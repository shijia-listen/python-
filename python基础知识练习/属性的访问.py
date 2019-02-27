class Programer(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __getattribute__(self, name):
        eturn super(Programer,self).__getattribute__(name)
    def __setattr__(self, name, value):
        self.__dict__[name]=value
if __name__ == '__main__' :
    p=Programer('Jenny',22)
    print p.name
