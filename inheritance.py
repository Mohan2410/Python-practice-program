class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname,self.lastname)
class Student(Person):
    # pass
    def __init__(self,fname,lname):
        Person.__init__(self,fname,lname)

x = Person("Mohan","Gawande")
x.printname()
x = Student("Ajay","Gawande")
x.printname()