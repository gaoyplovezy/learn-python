#算法：递归求和
x = 0
sum = 0
n = 5
print("方式一：")
for i in range(1,n+1):
	print("(",end="")
	for j in range(i):
		x = x+1
		print("x:",x,sep="",end=",")
		sum = sum + x
		#print("sum:",sum,sep="",end=",")
	print(")")
print(sum)