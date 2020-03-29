#Author:zyx

product_list = {"there are products":[]}
user_list = {"":[]}
user_balance = {"":[]}
buy_list = {"":[]}

username = input("username:").strip()
password = input("password:").strip()
while True:
    with open('goods.txt','r',encoding="utf-8") as goods_list,\
            open('balance.txt','r+',encoding="utf-8") as balance,\
            open('userbuy.txt','r+',encoding="utf-8") as user_buy,\
            open('userinfo.txt','r+',encoding="utf-8") as user_info:
        for i in goods_list:
            product_list.setdefault(i.split()[0],i.split()[1])
        for i1 in user_info:
            user_list.setdefault(i1.split()[0],i1.split()[1])
        for i2 in balance:
            user_balance.setdefault(i2.split()[0],i2.split()[1])
        for i3 in user_buy:
            buy_list.setdefault(i3.split()[0],i3.split()[1:])
    if username in user_list:
        if password == user_list[username]:
            for index, j in enumerate(list(product_list.items())):
                print(index, j)
            print("your balance is",user_balance[username])
            choice = input("choice products>>").strip()
            if choice.isdigit():
                choice = int(choice)
                if int(product_list[list(product_list.keys())[choice]]) <=int(user_balance[username]):
                    user_balance[username] = int(user_balance[username]) - int(product_list[list(product_list.keys())[choice]])
                    buy_list[username].append(list(product_list.keys())[choice])
                    print("add \033[31;1m%s\033[0m to your shopping list, your balance is \033[31;1m%s\033[0m"%(list(product_list.keys())[choice],user_balance[username]))
                else:
                    print("the balance is not enough")
            elif choice == "q":
                f = open('userbuy.txt','a',encoding="utf-8")
                f.write(buy_list)
                print("there is your shopping list",buy_list[username])
                break
            #elif choice == ""
        else:
            print("password error")
    else:
        with open('userinfo.txt','a',encoding="utf-8") as user_write,\
                open('balance.txt','a',encoding="utf-8") as user_salary:
            user_write.write('\n'+username+' '+password)
            salary = input("input your salary:").strip()
            user_salary.write('\n'+username+' '+salary)


'''
shopping_list = []
salary = input("Input your salary:")
if salary.isdigit():
    salary = int(salary)
    while True:
        for index,i in enumerate(product_list):
            print(index,i)
        user_choice = input("选择要买的商品编号：")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(product_list) and user_choice >=0:
                info = product_list[user_choice]
                if info[1] <= salary:
                    shopping_list.append(info)
                    salary -= info[1]
                    print("Added \033[32;1m%s\033[0m into shopping cart,your current balance is \033[31;1m%s\033[0m"%(info[0],salary))
                else:
                    print("余额不足")
            else:
                print("无此商品")
        elif user_choice == 'q':
            print("---------shopping list------------")
            for i in shopping_list:
                print(i)
            print("your current balance is",salary)
            exit()
        else:
            print("输入错误")
'''






