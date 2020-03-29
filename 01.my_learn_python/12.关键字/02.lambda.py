'''
lambda的一些用法
知识点：
(1)map()：遍历序列，对序列中每个元素进行操作，最终获取新的序列,map()的返回值是iterators, 所以想要使用，只用将iterator转换成list即可， 比如list(map())
简而言之，map()接收一个函数f和一个list，并通过把函数f依次作用在 list 的每个元素上，得到一个新的iterators并返回
(2)reduce()：对于序列内所有元素进行累计操作，即是序列中后面的元素与前面的元素做累积计算（结果是所有元素共同作用的结果）
需要手工引入：from functools import reduce
(3)filter()：‘筛选函数’，filter()把传人的函数依次作用于序列的每个元素，然后根据返回值是True还是false决定保留还是丢弃该元素，返回符合条件的序列
'''
'''
1、分解元组并拼接
知识点：
(1)map() 函数语法：
map(function, iterable, ...)
参数：
function -- 函数
iterable -- 一个或多个序列
返回值：
迭代器
(2)list(map对象)可以获取map()函数转换后的值
'''
def lambda1():
	list1 = [(1,2,3),('a','b','c'),(4,5,6)]
	res = map(lambda x:list(map(str,x)),list1)
	#print("".join(map(str,res)))
	print(list(res))
lambda1()
#输出结果：[['1', '2', '3'], ['a', 'b', 'c'], ['4', '5', '6']]

'''
2、将元组的第一个元素为key，第二个元素为value，组成一个字典，进而组成字典列表
'''
def lambda2():
	list1 = [(1,2,3),('a','b','c'),(4,5,6)]
	res_diclist = map(lambda r:{r[0]:r[2]},list1)
	print(list(res_diclist))
	#输出结果：[{1: 3}, {'a': 'c'}, {4: 6}]
	res_tuplist = map(lambda r:(r[0],r[1]),list1)
	print(list(res_tuplist))
	#输出结果：[(1, 2), ('a', 'b'), (4, 5)]
lambda2()

'''
3、列表元素累加，这里使用reduce
'''
from functools import reduce
def lambda3():
	list1 = [1,2,3,4,5,6,7]
	res = reduce(lambda x,y:x+y,list1)
	print(res)
	list2 = [('a',1),('b',2),('c',3),('a',11)]
	#期望转成字典后，将key值相同的value值累加
	#未完成
	
lambda3()

#海龟画图(很有意思)
from turtle import *
def turtle():
	forward(100)
	left(120)
	forward(100)
	left(120)
	forward(100)
#turtle()
