#Author:zyx
import time


def timer(func):
    def deco(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)
        stop_time = time.time()
        print("the func run time is %s" % (stop_time-start_time))
    return deco


@timer  #test1 = timer(test1)
def test1():
    time.sleep(2)
    print("test1")
@timer
def test2(name,age):
    print("your info:",name,age)
test1()
test2("zyx",22)
