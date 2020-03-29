__author__ = "zyx"
import time,os
temp = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def outer(user,money):
    with open('%s\logs\%s.txt' % (temp, user), 'a', encoding="utf-8") as f:
        f.write("支出%s "%money + time.strftime('%Y-%m-%d %H:%M:%S\n'))


def inner(user,money):
    with open('%s\logs\%s.txt' % (temp, user), 'a', encoding="utf-8") as f:
        f.write("收入%s "%money + time.strftime('%Y-%m-%d %H:%M:%S\n'))


def logger(user):
    with open('%s\logs\%s.txt' % (temp, user), 'r', encoding="utf-8") as f:
        file = f.read()
        print(file)
