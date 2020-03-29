#基本数据类型
print("------基本数据类型------")
a,b,c = 1,2,'aa'
print(a,b,c)
print(id(a),id(b),id(c),sep=",")

#显示变量类型
print("------显示变量类型------")
print(type(a))
print(type(c))
print(isinstance(a,int))
print(isinstance(c,int))

'''
isinstance() 与 type() 区别：
	1、type() 不会认为子类是一种父类类型，不考虑继承关系。
	2、isinstance() 会认为子类是一种父类类型，考虑继承关系。
	如果要判断两个类型是否相同推荐使用 isinstance()。
'''
class A:
	pass
class B(A):
	pass
print(isinstance(A(),A))#True
print(type(A()) == A)#True
print(isinstance(B(),A))#True
print(type(B()) == A)#False

'''
del可以删除对象的引用
'''
del a

#使用*表达式获取任意长度的对象
list = [1,2,3,4,5,6,7,8,9,0]
s1,*ss,s2 = list
print(ss)
