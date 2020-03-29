#Author:zyx
import time


def consumer(name):
    print("%s准备吃包子啦！" % name)
    while True:
        baozi = yield
        print("包子[%s]来了，被[%s]吃了！" % (baozi, name))


def producer(name):
    c = consumer('A')
    c2 = consumer(name)
    c.__next__()
    c2.__next__()
    print("准备开始做包子！")
    for i in range(10):
        time.sleep(1)
        print("做了一个包子，分两半！")
        c.send(i)
        c2.send(i)

producer('zyx')