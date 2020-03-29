voice = ['a','e','i','o','u']
word = input("here,input your word:")
#dict = {'e':0,'i':0,'e':0,'o':0,'u':0,'a':0}
dict = {}
for key in voice:
    dict[key] = 0

for letter in word:
    if letter in voice:
        dict[letter] +=1
print(dict)


#kv获取键值，sorted排序
for kv in sorted(dict):
    print(kv,dict[kv])

print()

#items内置方法可以返回一个键值对列表，然后将键值赋给k，值赋给v
for k,v in sorted(dict.items()):
    print(k,v)
