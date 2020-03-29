import time
import random

def zsFunc(ff):
	def contTime():
		startTime = time.time()
		age = ff()
		endTime = time.time()
		msecs = (endTime - startTime)*1000
		#print("执行等待时间",msecs,"秒")
		print("年龄：",age)
		if age >50 :
			print("年龄太大了")
		else:
			print("年龄合适")
	#这个return看不懂
	return contTime




#打印hello world!，但是，中间会随机休眠x秒
@zsFunc
def func():
	print("hello",end=" ")
	time.sleep(random.randint(1,6))
	print("world!")
	return random.randint(1,99)

s = func()
print(s)