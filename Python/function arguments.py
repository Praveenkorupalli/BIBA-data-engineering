#default arguments
print("default arguments: ")
def myfun(x,y=50):
    print("x:",x)
    print("y:",y)
myfun(10)

#keyword arguments
print("keyword arguments:")
def student(firstname,lastname):
    print(firstname,lastname)
student(firstname='hexa',lastname='practice')
student(lastname='practice',firstname='hexa')


#positional arguments
print("positional arguments:")

def nameAge(name,age):
    print("hi,I am",name)
    print("my age is",age)
print("case-1")
nameAge("suraj",19)
print("\ncase-2")
nameAge(19,"suraj")

#arbitrary keyword arguments:

#non-keyword arguments
print("\nnon-keyword arguments:")
def myfun(*argv):
    for arg in argv:
        print(arg)
myfun('hello','welcome','to','hexaware')

def add(*args):
   s=0
   for x in args:
      s=s+x
   return s
result = add(10,20,30,40)
print (result)

def avg(first, *rest):
   second=max(rest)
   return (first+second)/2
   
result=avg(40,30,50,25)
print (result)

#keyword arguments
print("\nkeyword arguments")

def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
 
myFun(first='Hexa', mid='for', last='Hexa')

def addr(**kwargs):
   for k,v in kwargs.items():
      print ("{}:{}".format(k,v))
print ("pass two keyword args")
addr(Name="John", City="Mumbai")
print ("pass four keyword args")
# pass four keyword args
addr(Name="Raam", City="Mumbai", ph_no="9123134567", PIN="400001")

def percent(math, sci, **optional):
   print ("maths:", math)
   print ("sci:", sci)
   s=math+sci
   for k,v in optional.items():
      print ("{}:{}".format(k,v))
      s=s+v
   return s/(len(optional)+2)
result=percent(math=80, sci=75, Eng=70, Hist=65, Geo=72)
print ("percentage:", result)