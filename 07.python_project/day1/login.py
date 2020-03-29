#Author:zyx

user_black_list = []
black_temp_list = []
user_list = {}
with open('userinfo.txt','r+',encoding="utf-8") as file1,open('buser.txt','r',encoding="utf-8") as file2:
    user_black_list = file2.read().split()
    for i in file1:
        user_list.setdefault(i.split()[0],i.split()[1])
while True:
    username = input("输入用户名:")
    password = input("输入密码:")
    if username in user_black_list:
        print("用户已锁定")
        continue
    elif username in user_list:
        if password == user_list[username]:
            print("登陆成功，欢迎\033[31;1m%s\033[0m"%(username))
            break
        else:
            print("密码错误")
            black_temp_list.append(username)
            if black_temp_list.count(username) == 3:
                break
    else:
        print("无此用户")
if black_temp_list.count(username) == 3:
    user_black_write = open("buser.txt","a",encoding="utf-8")
    user_black_write.write(username+' ')
    user_black_write.close()
    print("用户已锁定")

