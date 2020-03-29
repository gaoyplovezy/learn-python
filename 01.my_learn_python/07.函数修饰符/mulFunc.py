#class aplClass:
'''
1、将一个函数放在另一个函数中返回
'''
def apply(func: object,value:object) -> object:
	return func(value)

res = apply(type,10)
res = apply(print,10)
res = apply(id,10)
res = apply(type,apply)
print(res)
print("=========myFunc===========")
'''
2、使用*接收一个任意的参数表，即，允许一个函数可以接收任意数量的参数
'''
#使用*字符表示任意数字，并结合一个参数名(按惯例使用args)
def myFunc(*args):
	for a in args:
		print(a,end=' ')
	if args:
		print('args')

myFunc(1,1,2,'',3,2)
'''
注意：如果向myFunc提供一个列表做为参数，这个列表(尽管可能包含多个值)会被处理成一项(见：myFunc(value))，
为了指示解释器展开这个列表，使列表项作为一个单独的参数，调用函数时要在列表名前加*作为前缀(见：myFunc(*value))
'''
value=[1,2,3,4,5,6,11]
myFunc(value)
myFunc(*value)
print("=======myFunc2=============")
'''
3、使用**接收任意多个关键字参数，Python使用**展开一个关键字参数集合，通常使用kwargs参数名和**相连
'''
def myFunc2(**kwargs):
	for k,v in kwargs.items():
		print(k,v,sep='->',end=' ')
	if kwargs:
		print('kwargs')
myFunc2(a=1,b='b')
myFunc2()
dic2={'a':1,'b':2,'c':'ccc'}
myFunc(dic2)
'''
注意：
1、通过在参数前加**，意味着告诉解释器要把这个字典处理为键/值的集合，就好像是给方法传入了3个单独的关键字参数
2、不能myFunc2(dic2)，这样会报错
'''
myFunc2(**dic2)
print("=======myFunc3=============")
'''
4、综合*和**，写接收任意数量和类型的参数
'''
def myFunc3(*args,**kwargs):
	if args:
		for a in args:
			print(a,end=' ')
		print()

	if kwargs:
		for k,v in kwargs.items():
			print(k,v,sep='->',end=' ')
		print()

myFunc3(*value,**dic2)