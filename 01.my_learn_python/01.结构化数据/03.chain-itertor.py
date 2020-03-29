'''
多个对象同时遍历，下面的方式1和方式2要求类型必须一致，如果数据再大一点，那么消耗的内存也会增多；
方式3是通过创建迭代器的方式依次返回可迭代的对象
'''
'''
方式1：类型相同且各元素类型也相同
'''
print('-------方式1-------')
list1 = [1,2,3,4,5]
list2 = [6,7,8,9]
list3 = list1 + list2
for x in list3:
	print(x)

'''
方式2：类型相同且各元素类型不同
'''
print('-------方式2-------')
list21 = [1,2,3,4,5]
list22 = ['a','b','c']
list23 = list21 + list22
for x in list23:
	print(x)

'''
方式3：类型不同
'''
#不是逐一元素遍历，所以是个错误的方式
print('-------方式3-------')
list31 = [1,2,3,4,5]
tup32 = ('a','b','c','d')
for x in (list31,tup32):
	print(x)

#chain通过创建迭代器，依次返回可迭代对象的元素
from itertools import chain
for x in chain(list31,tup32):
	print(x)