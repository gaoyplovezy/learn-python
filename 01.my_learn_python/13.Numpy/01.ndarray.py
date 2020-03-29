import numpy as np

l1 = [1,2,3,4,5,6,7,8]
print(type(l1))

'''
dtype如果使用numpy的数据类型的时候，需要加np.，否则会认为是python的数据类型
'''
l2 = np.array(l1,dtype=np.complex_)
print(type(l2))
print('l2:',l2)

dt = np.dtype([('age',np.int8),('sex',np.bool_)])
a = np.array([(10,11),(20,21),(30,0)],dtype=dt)
print(a['age'])
print(a['sex'])
