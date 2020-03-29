'''
该功能读取todos.txt文件后，将数据放入嵌套列表中
'''

#1、向todos.txt文件中写入多行文字，每行文字的多个输入见用|分隔
from datetime import datetime
import random
str = '恭喜发财！'
with open('todos.txt','w') as inputfile:
	for i in str:
		print(i,datetime.today(),random.randint(1,datetime.today().minute),file=inputfile,sep='|')

#2、读取todos.txt文件，将结果放入嵌套list中
'''方式一：
contends = []
with open('todos.txt') as readfile:
	for line in readfile:
		contends.append([])
		contends[-1] = line.split('|')
'''
'''
方式二：
'''
contends = []
with open('todos.txt') as readfile:
	for line in readfile:
		contends.append([])
		for char in line.split('|'):
			contends[-1].append(char)



print(contends)