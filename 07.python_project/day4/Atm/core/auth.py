__author__ = "zyx"
import os
temp = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def auth(func):
    def atmlogin(*args,**kwargs):
        '''Atm装饰器'''
        info = {}
        pswd = input("请输入密码:").strip()
        with open('%s\core/user.txt' % temp, 'r', encoding="utf-8") as f:
            file = f.read()
            info = eval(file)
        while True:
            if pswd == info[args[0]][0]:
                print("你的余额为%s" %info[args[0]][1])
                func(*args,**kwargs)
                break
            else:
                pswd = input("密码错误，请重试:").strip()
                continue
    return atmlogin


def func(user):
    with open('%s\core/user.txt' % temp, 'r', encoding="utf-8") as f, \
            open('%s\core/blacklist.txt' % temp, 'r', encoding="utf-8") as b:
        file = f.read()
        info = eval(file)
        black_list = b.read().split(' ')
    while True:
        if user in info:
            if user in black_list:
                print("账户已被冻结，请联系管理员！")
                user = input("请输入用户名：")
                continue
            else:
                break
        else:
            print("无效的用户名!")
            user = input("请输入用户名:").strip()
            continue