#Author:zyx

age = 20
def change_name(name):
    global age  #修改全局变量  最好不用
    age = 21
    print("before change:",name)
    name = 'ZYX'
    print("after change:",name)
name = 'zyx'
change_name(name)
print(name,age)