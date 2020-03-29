l1=[1,2,3,4]
l2=['a','b','c','d']
for i in zip(l2,l1):
	print(i)
print("---"*20)

d1={'f':3,'j':2,'k':3}
for k in sorted(zip(d1.values(),d1.keys())):
	print(k)
dd = zip(d1.values(),d1.keys())
dd_min = min(dd)
print("最小值：",dd_min)
print("---"*20)

list2 = [('a',1),('b',2),('c',3),('a',11)]
for k in zip(list2):
	print(k)