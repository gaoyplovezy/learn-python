#Author:zyx

'''
import sys
#print(sys.path)  打印环境变量
print(sys.argv)
print(sys.argv[2])
'''

'''import os
#cmd_res = os.system("dir")  #执行命令，不保存结果
cmd_res = os.popen("dir").read()
print("-->",cmd_res)

os.mkdir("new_dir")'''

a = "2"
i = int(a)
print("1.%s  2.%s"%(a,i))

