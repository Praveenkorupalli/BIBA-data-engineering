file=open('file handling.txt','r')
print(file.read())

f=open('file handling.txt','r')
for each in f:
    print(each)
    
file=open('nested loop.py',"r")
print(file.read(15))

#split function
with open("file handling.txt",'r') as file:
    data=file.readlines()
    for line in data:
        word=line.split()
        print(word)

#write function

files=open("file_handling.txt",'w')
files.write('this is the write command')
files.write('it allows to write in a particular file')
files.close()

with open("file_handling.txt",'w') as f:
    f.write("\n hello world!!")
    
#append

file=open("file_handling.txt",'a')
file.write('this will add a new line')
file.close()

#try and except

a=[45,18,7]
try:
    print('second element= %d' %(a[1]))
    
    print('fourth element=%d' %(a[3]))
except:
    print('an error occured')