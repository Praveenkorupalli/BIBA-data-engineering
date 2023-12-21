class bird():
    def intro(self):
        print("type of birds:")
        
    def flight(self):
        print("all birds cannot fly")

class sparrow(bird):
    def flight(self):
        print("sparrows can fly")

class ostrich(bird):
    def flight(self):
        print('ostrich cannot fly')
        
obj1=bird()
obj2=sparrow()
obj3=ostrich()

obj1.intro()
obj1.flight()

obj2.intro()
obj2.flight()

obj3.intro()
obj3.flight()

#method overriding
class Father():
    def transportation(self):
        print('cycle')

class son(Father):
    def transportation(self):
        print('bike')

obj=son()
obj.transportation()

class Parent(): 
      
    # Constructor 
    def __init__(self): 
        self.value = "Inside Parent"
          
    # Parent's show method 
    def show(self): 
        print(self.value) 
          
# Defining child class 
class Child(Parent): 
      
    # Constructor 
    def __init__(self): 
        self.value = "Inside Child"
          
    # Child's show method 
    def show(self): 
        print(self.value) 
          
          
# Driver's code 
obj1 = Parent() 
obj2 = Child() 
  
obj1.show() 
obj2.show() 




#method overloading - method name should be same , arguments must be different

class moverload():
    def display(self,a=None,b=None):
        print(a,b)
obj=moverload()
obj.display()
obj.display(10)
obj.display(10,20)