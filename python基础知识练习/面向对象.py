class Programer(object):
    hobby='Play Computer'
    def __init__(self,name,age,weight):
        self.name=name
        self._age=age
        self.__weight=weight
    @classmethod
    def get_hobby(cls):
        return cls.hobby
    @property
    def get_weight(self):
        return self.__weight
    def self_introduction(self):
        print 'My name is %s \n I am %s years old\n'%(self.name,self._age)
#programer=Programer('jenny',22,90)
#programer.self_introduction()
#print programer.get_weight
#print Programer.get_hobby()
class BackendProgramer(Programer):
    #def __init__(self,name,age,weight,language):
        #super(BackendProgramer,self).__init__(name,age,weight)
    def __init__(self,name,age,weight,language):
        Programer.__init__(self,name,age,weight)
        self.language=language
    def self_introduction(self):
        print'My name is %s\n My favorite language is %s\n'%(self.name,self.language)
def introduce(programer):
    if isinstance(programer,Programer):
        programer.self_introduction()
        
        
if __name__=='__main__':
    programer=Programer('liming',23,140)
    print dir(programer)
    print programer.__dict__
    print type(programer)
    backend_programer=BackendProgramer('Jenny',21,90,'python')
    introduce(programer)
    introduce(backend_programer)
   
    
