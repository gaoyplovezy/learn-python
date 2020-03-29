__author__ = "zyx"
import auth,log
import business
import management

user = input("请输入用户名:").strip()
auth.func(user)
temp = False
while not temp:
    print(
        '''
        1.提现
        2.还款
        3.转账
        4.账户管理
        5.查询流水
        6.退出
        '''
    )
    choice = input("请输入要做的事：").strip()
    if choice == '1':
        business.cash(user)
    elif choice == '2':
        business.pay_back(user)
    elif choice == '3':
        business.transfer(user)
    elif choice == '4':
        print(
            '''
            1.添加账户
            2.冻结账户
            '''
        )
        c = input("请输入要做的事：").strip()
        management.func1(c,user)
        break
    elif choice == '5':
        log.logger(user)
    elif choice == '6':
        temp = True
        print("退出成功！")
    else:
        choice = input("输入错误，请重新选择:").strip()
        continue
