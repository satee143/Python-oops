class Person(object):

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
        
    @classmethod
    def get_person(cls, first_name):
        return cls(first_name, "")
        
        
p=Person('raju')
print(p.first_name)