import numpy as np


'''
该方法可能会因为自然常数e的指数太大，而导致溢出

def softmax(a):
	exp_a = np.exp(a)
	exp_sum_a = np.sum(exp_a)
	print(exp_sum_a)
	y = exp_a/exp_sum_a
	return y
'''

def softmax(a):
	#获取输入信号中的最大值
	c = np.max(a)
	#修正，输入信号减去输入信号中的最大值
	exp_a = np.exp(a-c)
	exp_sum_a = np.sum(exp_a)
	print(exp_sum_a)
	y = exp_a/exp_sum_a
	return y

#print(softmax(np.array([0.3,2.9,4.0])))
print(softmax(np.array([10000,1,2])))
