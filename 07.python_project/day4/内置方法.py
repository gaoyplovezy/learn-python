# Author:zyx

# print(all([1,-5,3]))  # 任意为假就为假，全部为真才为真
# print(any([1,-5,3]))  # 任意为真就为真，全部为假才为假
# print(bin(255))  # 转换二进制

# b = bytearray('abcde',encoding="utf-8")  # 转换成可修改
# print(b[1])
# def a():pass
# print(callable(a()))  # 是否可调用（）
# print(chr(98))  # 返回ascii对应的字符
# print(ord('b'))  # 返回字符对应的ASCII码

# a = 10
# b = 5
# print(f" a+b={a+b} and a*b={a*b}")  # f后字符串{}中可以输入变量
#
# def hello(name):
#     print(f"hello,{name}")
#
# hello("alex")

# print(divmod(5, 2))  # 5除2  返回商和余数

# a, b = 1, 2
# c = 'a+b'
# print(eval(c))  # 将字符串转化为执行语句

# exec()  # 将字符串转化为执行语句

# calc = lambda n:print(n)  # 匿名函数  用完就释放内存
# calc(2)

#res = filter(lambda n:n>5, range(10))  # 从后面中筛选出符合前面条件
# res = map(lambda n:n*2, range(10))  # 相当于[ i*2 for i in range(10)]
# res = [lambda i:i*2 for i in range(10)]

# import functools
# res = functools.reduce( lambda x,y:x+y, range(10))  #将x+y的值赋给x，继续加
# print(res)

# a = frozenset([1,2,3,4,4,5,6,1,23])  #不可变集合，不可修改

# print(globals())  # 把文件中所有全局变量以字典形式打印，变量名是key，变量值是value
# locals()  # 同globals 是局部变量
# hex()  # 转16进制
# oct()  # 转8进制
# pow(2,3)  # 2的3次方
# round(1.31546,2)  # 保留2位

# a = {6:2,8:0,1:4,-5:6,99:11,4:22}
# print(sorted(a.items()))  # 将字典按key排序并转化成列表
# print(sorted(a.items(),key=lambda x:x[1]))  #将字典按value排序并转化成列表

# a = [1,2,3,4]
# b = ['a','b','c','d']
# for i in zip(a,b):  # 连接两个列表一一对应
#     print(i)

# __import__('decorator')  # 引用一个只知道字符串格式的模块




