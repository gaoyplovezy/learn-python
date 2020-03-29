'''
标准库提供了一个名为sys的模块，可以利用这个模块访问解释器内部信息。
exc_info：会提供当前处理的异常的相关信息。调用exc_info时，这个函数会返回一个包括3个值的元组，其中第一个值指示异常的类型；
第二个值详细描述异常的值；第三个值包括一个回溯跟踪对象，允许访问回溯跟踪消息。
'''
import sys
try:
	1/0
except:
	err = sys.exc_info()
	for e in err:
		print(e)
print('=====方式二===========')
try:
	2/0
except Exception as err:
	print(err)