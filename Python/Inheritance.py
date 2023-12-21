class Person(object):
    def __init__(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)
        
    def deatils(self):
        print("my name is {}".format(self.name))
        print("idnumber is {}".format(self.idnumber))
        
class Employee(Person):
    def __init__(self,name,idnumber,salary,post):
        self.salary=salary
        self.post=post
        
        Person.__init__(self,name,idnumber)
    def details(self):
     
        print("salary is {}".format(self.salary))
        print("post IS {}".format(self.post))
        
a=Employee('rohit',784646,40090,"intern")
    
a.display()
a.details()

#single level Inheritance

class Parent():
    def quality(self):
        print('\ninside father class')
        
class child(Parent):
    def aim(self):
        print("\ninside child  class")
        
obj=child()
obj.quality()
obj.aim()

#multi-level inheritance

class manager():
    def final_review(self):
        print("final review")
class reviewer(manager):
    def review(self):
        print("reviewing...")
class writer(reviewer):
    def writes(self):
        print("writes code")
        
obj=writer()
obj.final_review()
obj.review()
obj.writes()

#multiple inheritance

class father():
    def pdisplay(self):
        print('inside father class')
class mother():
    def mdisplay(self):
        print('inside mother class')
class child(father,mother):
    def cshow(self):
        print("\ninside child class")

obj=child()
obj.pdisplay()
obj.mdisplay()
obj.cshow()

#heirarchial inheritance
class parent():
    def show(self):
        print("\ninside parent class")
class child1(parent):
    def c1display(self):
        print("inside child1 class")
        
class child2(parent):
    def c2dis(self):
        print("inside child2 class")
        
obj1=child1()
obj1.show()
obj1.c1display()

obj2=child2()
obj2.show()
obj2.c2dis()


        
