import pickle as plk
import numpy as np
'''
1、pickle模块的读写模式都是wb、rb类型的，文件需要以wb、rb模式打开
'''


def pick_with_dump() :
	with open ('pickle.txt','wb') as f:
		s = "啦\n啦啦"
		plk.dump(s,f)
		l = [1,2,3,4,5,6]
		plk.dump(l,f)
		
		print("--------------")
		sbytes = plk.dumps(s)
		print(sbytes)
		
def pick_with_load():
	with open ('pickle.txt','rb') as f:
		l = plk.load(f,encoding='ISO 8859-1')
		l2 = plk.load(f)
		print(l)
		print(l2)

#被pickle序列化后的文件内容不可读，但是反序列化后可以取出数据
def pick_file_dump():
	f = open('pickle.txt','wb')
	x = np.arange(-5,5,0.1)
	plk.dump(x,f)

	f.close()

def pick_file_load():
	f = open('pickle.txt','rb')
	x = plk.load(f)
	print(x)
	f.close()

pick_with_dump()
pick_with_load()
