list=[10,20,30,40,50,60,70,80,90]

print('original list:',list)
print(list[::2])
print(list[:8:2])
print(list[2:9:3])

print(list[::-1])
print(list[:-2:-2])
print(list[:1:-1])
print(list[:2:-2])

newlist=list[2:6:1]+list[:8:2]
print("newlist:",newlist)

list[2:4]=["hex",'for','hex','!']
print("modified list:\n",list)