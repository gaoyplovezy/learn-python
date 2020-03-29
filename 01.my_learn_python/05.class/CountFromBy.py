class CountFromBy:
	def increase(self) -> None:
		self.val += self.incr
		print(self.val)

	'''
	初始化方法：
	1、初始化val和Incr变量，因为如果不初始化increase方法执行的时候就会报错
	2、定义初始方法后，实例化类：g = CountFromBy(100,20)
	'''
	def __init__(self,v:int,i:int) -> None:
		#pass
		#使用v和i的值分别初始化类的属性
		self.val = v
		self.incr = i
	'''
	初始化方式(带有默认值)：
	定义初始方法后，实例化类：g = CountFromBy(100,20)
	或：g = CountFromBy()
	def __init__(self,v:int = 0,i:int = 1) -> None:
		self.val = v
		self.incr = i
	'''
	#返回返回一个字符串
	def __repr__(self) -> str:
		return str(self.val)

