import os
import csv
#设置需要使用的文件所在目录
os.chdir('C:/10E/OneDrive/03.充电/06.开发语言/03.Python/98.工程存档/01.workspace_idle/11.高级迭代')
with open('buzzers.csv') as raw_data:
	print(raw_data.read())

#下面这种是将CSV文件中的每行数据转换为一个列表
#使用"csv.reader"一次读取一行数据
with open('buzzers.csv') as data:
	for line in csv.reader(data):
		print(line)


with open('buzzers.csv') as data:
	for line in csv.DictReader(data):
		print(line)