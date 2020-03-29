# Author:zyx

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        # print(b)
        yield b  # 把函数变为生成器
        a, b = b, a+b
        n = n + 1
    return 'done'
g = fib(6)
while True:
    try:
        x = next(g)
        print('g:',x)
    except StopIteration as e:
        print('Generator return value:',e.value)
        break

# f = fib(10)
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())