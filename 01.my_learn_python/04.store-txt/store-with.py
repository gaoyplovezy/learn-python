'''
with语句符合python中内置的一个编码约定，这称为上下文管理协议，使用with后，解释器会在需要的时候调用close来关闭文件
'''
with open ('todos.txt') as tasks:
	for chore in tasks:
		print(chore,end='')
	'''
	print('以下为一次性读取：')
	contents = tasks.read()
	print(contents)
	'''

with open('todos.txt','w') as todos:
	print('日志1','日志2','日志3','日志4','日志5',file=todos,sep='|')

'''
问题：readtodos被读取之后，就无法再次读取了
'''
with open('todos.txt','r') as readtodos:
	print(readtodos)
	contents = readtodos.read()
	print(readtodos)
	str_list = contents.split('|')
	print(str_list)