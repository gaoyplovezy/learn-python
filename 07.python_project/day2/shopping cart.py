#Author:zyx
product_list = [
    ('Iphone',5800),
    ('Mac Pro',9800),
    ('Bike',800),
    ('Coffee',31),
    ('Book',120),
]
temp = False
user_list = {}
buy_list = {}
with open('userinfo.txt','r',encoding="utf-8") as user_info:
    userinfo = user_info.read()
user_list = eval(userinfo)
username = input("username:").strip()
password = input("password:").strip()
while True:
    if username in user_list:
        if password in user_list[username]:
            salary = int(user_list[username][password])
            print("\033[31;1mWelcome! Your balance is %s\033[0m"%(salary))
            break
        else:
            password = input("Password error!Please try again!")
            continue
    else:
        password_salary = {}
        salary = input("Input your salary:").strip()
        if salary.isdigit():
            password_salary[password] = salary
            user_list[username] = password_salary
        else:
            print("Please input number")
        with open('userinfo.txt','w',encoding="utf-8") as file:
            file.seek(0)
            file.write(str(user_list))
with open('userbuy.txt','r+',encoding="utf-8") as buylist:
    buy_list = eval(buylist.read())
if username in buy_list:
    shopping_list = buy_list[username]
else:
    shopping_list = []
    buy_list[username] = shopping_list
while not temp:
    for index, j in enumerate(product_list):
        print(index, j)
    choice = input("Choice the number of the product>>>").strip()
    if choice.isdigit():
        choice = int(choice)
        if choice<=len(product_list):
            if salary>=int(product_list[choice][1]):
                salary = salary - int(product_list[choice][1])
                user_list[username][password] = str(salary)
                print(user_list)
                print("\033[31;1mAdd %s into your shopping list, and your balance is %s\033[0m"%(product_list[int(choice)],salary))
                shopping_list.append(product_list[choice])
            else:
                print("Your balance is not enough!")
        else:
            print("Please input the number in list!")
    elif choice == 'list':
        print("\033[31;1mYour shopping list is %s\033[0m"%shopping_list)
    elif choice == 'q':
        with open('userbuy.txt','w',encoding="utf-8") as buy,\
                open('userinfo.txt','w',encoding="utf-8") as u:
            u.write(str(user_list))
            buy.write(str(buy_list))
        temp = True
        print("\033[31;1mYour shopping list is %s, and your balance is %s\033[0m"%(shopping_list,salary))
    else:
        print("Input error! Please input again")


