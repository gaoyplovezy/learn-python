#Author:zyx

def test(*args): #参数组
    print(args)
test('zyx')
test(*[1,2,3,4,5])

def test2(**kwargs):
    print(kwargs)
test2(name = 'zyx',age = 20)
test2(**{'name':'zyx','age':20})
