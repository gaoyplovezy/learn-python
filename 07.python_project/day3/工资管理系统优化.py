#Author:zyx
staff = {}
temp = False
with open('info.txt','r',encoding="utf-8") as file:
    for i in file:
        staff.setdefault(i.split()[0],i.split()[1])


def select():
    '''查询员工信息'''
    name = input("请输入要查询的员工姓名:").strip()
    if name in staff:
        print("%s的工资是:%s" % (name, staff[name]))
    else:
        print("没有这个员工！")


def update(name,salary):
    '''修改员工工资'''
    with open('info.txt', 'r', encoding="utf-8") as file,\
            open('info.bak', 'w', encoding="utf-8") as bak:
        for line in file:
            if name in line:
                line = line.replace(staff[name],salary)
                staff[name] = salary
            bak.write(line)
    with open('info.txt', 'w', encoding="utf-8") as a,\
            open('info.bak', 'r', encoding="utf-8") as b:
        t = b.read()
        a.write(t)


def upd():
    '''修改功能'''
    x = input("请输入要修改的员工姓名和工资，用空格分隔:").strip()
    if x.split()[0] in staff:
        update(x.split()[0], x.split()[1])
        print("修改成功！")
    else:
        print("没有这个员工！")

def add(people):
    '''增加员工记录'''
    with open('info.txt','a',encoding="utf-8") as f:
        f.write('\n'+people)

def a():
    people = input("请输入要增加的员工姓名和工资，共空格分割:").strip()
    if people.split()[0] in staff:
        print("该员工存在!")
    else:
        add(people)
        staff.setdefault(people.split()[0],people.split()[1])
        print("增加成功！")

while not temp:
    print('''
    1. 查询员工工资
    2. 修改员工工资
    3. 增加新员工记录
    4. 退出''')
    choice = input(">>>").strip()
    if choice.isdigit():
        if choice == '1':
            select()
        elif choice == '2':
            upd()
        elif choice == '3':
            a()
        elif choice == '4':
            temp = True
            print("再见！")
        else:
            print("请输入列表中的序号!")
    else:
        print("输入错误，请重新输入!")
