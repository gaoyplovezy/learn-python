__author__ = "zyx"
import auth
import time,os
temp = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def add():
    '''增加账户'''
    info = {}
    with open('%s/core/user.txt' % temp, 'r', encoding="utf-8") as f:
        file = f.read()
        info = eval(file)
    while True:
        username = input("请输入要新增的用户名：").strip()
        if username in info:
            print("用户名存在")
            continue
        else:
            password_money = []
            password = input("请输入新增用户的密码：").strip()
            money = input("请输入您的余额：").strip()
            password_money.append(password)
            password_money.append(money)
            info.setdefault(username, password_money)
            print("新增成功！")
            with open('%s/core/user.txt' % temp, 'w', encoding="utf-8") as b, \
                    open('%s\logs\log.txt' % temp, 'a', encoding="utf-8") as f:
                b.write(str(info))
                f.write("新增操作成功 " + time.strftime('%Y-%m-%d %H:%M:%S\n'))
            break


@auth.auth
def freeze(user):
    '''冻结账户'''
    black_list = []
    with open('%s/core/blacklist.txt' % temp, 'r', encoding="utf-8") as f:
        black_list = f.read().split(',')
    black_list.append(user)
    with open('%s/core/blacklist.txt' % temp, 'w', encoding="utf-8") as b, \
            open('%s\logs\log.txt' % temp, 'a', encoding="utf-8") as f:
        b.write(' '.join(black_list))
        f.write("冻结操作成功 " + time.strftime('%Y-%m-%d %H:%M:%S\n'))
    print("冻结成功")


def func1(num,user):
    '''账户管理'''
    if num == '1':
        add()
    elif num == '2':
        freeze(user)
    else:
        print("没有这个选项")
