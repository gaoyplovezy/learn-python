import numpy as np

def fnc_arr1():
	x = np.array([[1,2,3],[4,5,6],[7,8,9]])
	print(x)
	print(np.ndim(x))
	print(np.shape(x))
	print("--------------")
	a = np.zeros(shape=(5,3))
	print(a)
	print(np.ndim(a))


def fnc_arr2x2():
	x = np.array([[1,2],[3,4]])
	y = np.array([[5,6],[7,8]])
	z = np.dot(x,y)
	print(z)

def fnc_arr2x1():
	x = np.array([[1,2],[3,4],[5,6]])
	y = np.array([7,8])
	print(np.shape(x))
	print(np.shape(y))
	z = np.dot(x,y)
	print(z)

fnc_arr2x1()