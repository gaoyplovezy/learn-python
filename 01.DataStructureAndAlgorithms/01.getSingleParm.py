'''
1.1 将序列分解为单独的变量
说明：
1、变量的数量必须和元素的数量一致
2、只要对象是可迭代的，均可以执行分解操作，包括：元组、列表、字符串、文件、迭代器、生成器
3、对于不需要的元素，可以使用不常用的变量名获取，以便丢弃，如： _

'''

def getAll():
    #元组
    tup1 = (4,5)
    x,y = tup1
    print("x=",x,"  ","y=",y)

    #list
    list1 = ['ACMS',50,91.2,(1,2,3,4,5,6)]
    a,b,c,d = list1
    print("a=",a," ","b=",b," ","c=",c," ","d=",d)

    #string
    str1 = "hello"
    a,b,c,d,e = str1
    print("c=",c)
    _,_,m,_,_ = str1 #使用_丢弃不需要的元素
    print("m=",m)
#getAll()

'''
1.2 从任意长度的可迭代对象中分解元素
1、使用python中的“*表达式”解决N个元素的迭代问题，*表达式获取到的数据都是一个list
2、*表达式可以用在：第一个位置、中间位置、最后一个位置
'''
#示例1：去掉一个最高分、一个最低分，其他分数求平均值
def drop_first_last(grades):
    first,*middle,last = grades
    sum1 = sum(middle)
    size = len(middle)
    return sum1/size
grades = [100,98,87,86,60,59,13,11]
print(drop_first_last(grades))


