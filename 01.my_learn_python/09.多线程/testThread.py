'''
有问题：st的值是1个a，代码可以正常执行，如果是多个就会报错
'''
from threading import Thread
def func(v:str) -> None:
	print(v)

try:
	st = 'a'
	t = Thread(target=func,args=(st))
	t.start()
except Exception as err:
	print(err)