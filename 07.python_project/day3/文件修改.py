#Author:zyx
import sys
# p = sys.argv[1]
# q = sys.argv[2]
# print(p,q)
with open('test','r',encoding="utf-8") as f,\
    open('test.bak','w',encoding="utf-8") as p:
    file = f.read()
    p.write(file)
