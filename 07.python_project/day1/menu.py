#Author:zyx

province = {}
city = {}
with open('city.txt','r',encoding="GB2312") as city_list,\
        open('province.txt','r',encoding="GB2312") as province_list:
    for i in city_list:
        city.setdefault(i.split()[0],i.split()[1:])
    for j in province_list:
        province.setdefault(j.split()[0],j.split()[1:])
temp = False
while not temp:
    for i in province:
        print(i)
    p_input = input("请选择省:")
    if p_input in province:
        while not temp:
            for i1 in province[p_input]:
                print("\t",i1)
            c_input = input("请选择市:")
            if c_input in city:
                while not temp:
                    for i2 in city[c_input]:
                        print("\t\t",i2)
                    z_input = input("请选择区:")
                    if z_input in city[c_input]:
                        print("您选择的区域为:\033[41;1m%s%s%s\033[0m"%(p_input,c_input,z_input))
                    elif z_input == 'b':
                        print("返回选择市")
                        break
                    elif z_input == 'q':
                        temp = True
                        print("退出成功")
                    else:
                        print("没有这个区，请重新选择")
            elif c_input == 'b':
                print("返回选择省")
                break
            elif c_input == 'q':
                temp = True
                print("退出成功")
            else:
                print("没有这个市，请重新选择")
    elif p_input == 'q':
        temp = True
        print("退出成功")
    else:
        print("没有这个省，请重新选择")
