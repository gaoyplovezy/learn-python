#初始化集合方式一：
#vowels = {'a','u','i','e','e'}

#初始化集合方式二：
vowels = set('auiee')

word = 'hello world!'

#union取集合并集
u = vowels.union(set(word))
u_list = sorted(list(u))
print(u)
print(u_list)

#difference取在vowels集合而不在set(word)集合中的元素
d = vowels.difference(set(word))
print(d)

#intersection取集合交集
i = vowels.intersection(set(word))
print(i)

