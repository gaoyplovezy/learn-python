#Author:zyx
'''import copy
names = ["wo","shi","zhong","guo","ren"]
names2 = copy.deepcopy(names) #完全复制
print(names2)

print(names[0:-1])'''

name = "a123"
write1 = open('buser.txt','a',encoding="utf-8")
write1.write(name+',')
write1.close()
with open('buser.txt','r',encoding="utf-8") as file:
    name1 = file.read().split(',')
print(name1)

