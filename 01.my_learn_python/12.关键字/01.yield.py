'''
python中有一个非常有用的语法叫做生成器，所利用到的关键字就是yield。
有效利用生成器这个工具可以有效地节约系统资源，避免不必要的内存占用。
参考网址：
https://blog.csdn.net/mieleizhi0522/article/details/82142856
https://www.cnblogs.com/zhenlingcn/p/8337788.html
'''
def foo():
	print("starting----------")
	while True:
		res = yield 4
		print("res:",res)

if __name__ == '__main__':
	#1.程序开始执行以后，因为foo函数中有yield关键字，所以foo函数并不会真的执行，而是先得到一个生成器g(相当于一个对象)
	g = foo()
	#输出结果：(此时不会有输出)

	'''
	2.直到调用next方法，foo函数正式开始执行，先执行foo函数中的print方法，然后进入while循环。
	程序遇到yield关键字，可以把yield想象成return,return了一个4之后，程序停止，并没有执行赋值给res操作，此时next(g)语句执行完成
	'''
	print(next(g))
	#输出结果：
	#starting----------
	#4

	'''
	3、程序执行print("*"*20)，输出20个*
	'''
	print("*"*20)
	#输出结果：
	#********************

	'''
	4、执行下面的print(next(g)),这个时候和上面那个print(next(g))差不多，不过不同的是，
	这个时候是从刚才那个next程序停止的地方开始执行的，也就是要执行res的赋值操作，
	这时候要注意，此时赋值操作的右边是没有值的（因为刚才那个是return出去了，并没有给赋值操作的左边传参数），
	所以这个时候res赋值是None,所以接着下面的输出就是res:None。
	程序会继续在while里执行，又一次碰到yield,这个时候同样return出4，然后程序停止，print函数输出的4就是这次return出的4
	'''
	print(next(g))
	#输出结果：
	#res: None
	#4

	'''
	5、程序执行print(g.send(7))，程序会从yield关键字那一行继续向下运行，send会把7这个值赋值给res变量。
	由于send方法中包含next()方法，所以程序会继续向下运行执行print("res:",res)方法，然后再次进入while循环，
	程序执行再次遇到yield关键字，yield返回4后，程序再次暂停，直到再次调用next方法或send方法。
	'''
	print(g.send(7))
	#输出结果：
	#res: 7
	#4


'''
详解：
1、next()函数：从上一个入口/终止点开始，到yield结束，返回值是yield表达式的值。
2、send()函数：只能从yield之后开始，到下一个yield结束。这也就意味着第一次调用必须使用next()函数。
send()函数最重要的作用在于它可以给yield对应的赋值语句赋值，比如上面那一段代码中的res = yield 4，在next()函数取走yield 4后，
使用send(7)可以给res赋值
'''

