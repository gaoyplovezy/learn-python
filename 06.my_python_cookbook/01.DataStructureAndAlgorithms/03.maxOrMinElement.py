'''
1.4 找到最大或最小的N个元素
关键：
heapq模块中有两个函数：nlargest()和nsmallest()，适合元素较少的情况
'''
import heapq
#简单类型
nums = [1,2,3,4,5,6,-1,-3,-6,99,10.11,10.12]
nums = range(1,100)
maxN = heapq.nlargest(5,nums)
minN = heapq.nsmallest(5,nums)
print('maxN前5个:',maxN)
print('minN前5个:',minN)
print("-"*20)
#通过参数key，可以在复杂的数据结构上处理
portfolio = [
            {'name':'IBM','price':91,'emp':5000},
            {'name':'Oracle','price':80,'emp':700},
            {'name':'Apache','price':77,'emp':6000},
            {'name':'yusys','price':33,'emp':7000},
            {'name':'Haier','price':120,'emp':1234},
            {'name':'FK','price':91,'emp':680}          
            ]
max_proN = heapq.nlargest(3,portfolio,key=lambda s:s['price'])
min_proN = heapq.nsmallest(3,portfolio,key=lambda s:s['price'])
print('max_proN:',max_proN)
print('min_proN:',min_proN)
