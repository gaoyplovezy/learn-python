#Author:zyx
dect = {}
data = {}
with open('test','r+',encoding="utf-8") as file:
    f = file.read()
    data = eval(f)
    print(data)

