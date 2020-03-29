__author__ = "zyx"
import auth,log
import time,os
temp = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

@auth.auth
def cash(user):
    '''提现'''
    balance = {}
    with open('%s/core/user.txt' % temp, 'r', encoding="utf-8") as f:
        file = f.read()
        balance = eval(file)
    money = input("请输入要取的金额:").strip()
    while True:
        if money.isdigit():
            money = int(money)
            if money%100 == 0:
                if money*1.05 <= int(balance[user][1]):
                    balance[user][1] = int(balance[user][1]) - money*1.05
                    print("你的余额为%s"%balance[user][1])
                    log.outer(user,money)
                    with open('%s/core/user.txt' % temp, 'w', encoding="utf-8") as b, \
                            open('%s\logs\log.txt' % temp, 'a', encoding="utf-8") as f:
                        b.write(str(balance))
                        f.write("提现操作成功 " + time.strftime('%Y-%m-%d %H:%M:%S\n'))
                    break
                else:
                    print("余额不足")
                    break
            else:
                money = input("请输入100的整数倍:").strip()
                continue
        else:
            money = input("请输入金额:").strip()
            continue

@auth.auth
def pay_back(user):
    '''还款'''
    balance = {}
    with open('%s/core/user.txt' % temp, 'r', encoding="utf-8") as f:
        file = f.read()
        balance = eval(file)
    money = input("请输入要还的钱:").strip()
    while True:
        if money.isdigit():
            money = int(money)
            balance[user][1] = int(balance[user][1]) + money
            print("还款成功,你的余额为%s"%balance[user][1])
            log.inner(user,money)
            with open('%s/core/user.txt' % temp, 'w', encoding="utf-8") as b, \
                    open('%s\logs\log.txt' % temp, 'a', encoding="utf-8") as f:
                b.write(str(balance))
                f.write("还款操作成功 " + time.strftime('%Y-%m-%d %H:%M:%S\n'))
            break
        else:
            money = input("请输入金额：").strip()
            continue

@auth.auth
def transfer(user):
    '''转账'''
    balance = {}
    black_list = []
    with open('%s/core/user.txt' % temp, 'r', encoding="utf-8") as f, \
            open('%s/core/blacklist.txt' % temp, 'r', encoding="utf-8") as b:
        file = f.read()
        balance = eval(file)
        black_list = b.read().split(' ')
    username = input("请输入要转账的用户名：").strip()
    while True:
        if username in balance:
            if username in black_list:
                print("此账户已被冻结！")
            else:
                money = input("请输入要转账的金额：").strip()
                if money.isdigit():
                    money = int(money)
                    if money <= int(balance[user][1]):
                        balance[username][1] = int(balance[username][1]) + money
                        balance[user][1] = int(balance[user][1]) - money
                        print("转账成功！你的余额为%s"%balance[user][1])
                        log.inner(username,money)
                        log.outer(user,money)
                        with open('%s/core/user.txt' % temp, 'w', encoding="utf-8") as b, \
                                open('%s\logs\log.txt' % temp, 'a', encoding="utf-8") as f:
                            b.write(str(balance))
                            f.write("转账操作成功 " + time.strftime('%Y-%m-%d %H:%M:%S\n'))
                        break
                    else:
                        print("余额不足")
                        break
                else:
                    money = input("请输入金额:").strip()
                    continue
        else:
            print("用户不存在")
            break
