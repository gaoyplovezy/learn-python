voice = ['a','e','i','o','u']
word = input("here,input your word:")
dict = {}


for letter in word:
    if letter in voice:
        '''使用下面两行，替换if...elif
        if letter in dict:
            dict[letter] +=1
        elif letter not in dict:
            dict[letter] = 1
        '''
        dict.setdefault(letter,0)
        dict[letter] +=1
print(dict)


#kv获取键值，sorted排序
for kv in sorted(dict):
    print(kv,dict[kv])

print()

#items内置方法可以返回一个键值对列表，然后将键值赋给k，值赋给v
for k,v in sorted(dict.items()):
    print(k,v)
