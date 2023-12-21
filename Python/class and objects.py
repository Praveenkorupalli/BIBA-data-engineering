class Dog():
    pass
obj=Dog()



class Dog():
    attr1 = "mammal"
# Instance attribute
    def __init__(self, name):
        self.name = name
        
# Driver code
# Object instantiation
Rodger = Dog("snoopy")
Tommy = Dog("tommy")

# Accessing class attributes
print("Rodger is a {}".format(Rodger.__class__.attr1))
print("Tommy is also a {}".format(Tommy.__class__.attr1))

# Accessing instance attributes
print("My name is {}".format(Rodger.name))
print("My name is {}".format(Tommy.name))



class Dog:
    def __init__(self,name):
        self.name=name
    def speak(self):
        print("\nMy name is {}".format(self.name))
        
dog1=Dog('Tommy')
dog2=Dog('snoopy')

dog1.speak()
dog2.speak()
        