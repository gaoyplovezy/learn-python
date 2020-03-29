#Author:zyx

list_1 = set([1,3,4,5,8,4,3,5,9,11])
list_2 = set([0,2,5,45,74,3])
list_3 = set([1,3,4])
list_4 = set([123,456])
print(list_1)
#差集
print(list_1.difference(list_2))
#交集
print(list_1.intersection(list_2))
#并集
print(list_1.union(list_2))
#在集合内就删除，不在就不删
print(list_1.discard(11))
list_1.add(999)
print(list_1)
#有交集返回False，无交集返回True
print(list_1.isdisjoint(list_4))
#子集
print(list_3.issubset(list_1))
#父集
print(list_1.issuperset(list_3))
#对称差集
print(list_1.symmetric_difference(list_3))

