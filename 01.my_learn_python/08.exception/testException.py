'''
try一次，except多次
'''
try:
	with open('tt.txt') as f:
		print(f)
except FileNotFoundError:
	print('找不到tt.txt文件')
except PermissionError:
	print('没有权限执行')
#除去以上两个异常外的其他异常会在此处被捕获
except:
	print('其他异常')