#Author:zyx
import time
def logger():
    time_format = '%Y-%m-%d %X'
    time_current = time.strftime(time_format)
    with open('test','a',encoding="utf-8") as f:
        f.write('end\n')
def test1():
    print('test1:')
    logger()
def test2():
    print('test2:')
    logger()
def test3():
    print('test3:')
    logger()


