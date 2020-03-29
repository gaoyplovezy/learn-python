#Author:zyx

product_list = [
    ('Iphone',5800),
    ('Mac Pro',9800),
    ('Bike',800),
    ('Coffee',31),
    ('Book',120),
]
shopping_list = []
salary = input("Input your salary:")
if salary.isdigit():
    salary = int(salary)
    while 1:
        #for i in product_list:
         #   print(product_list.index(i),i)
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







