# Author:zyx

import os, sys
print(__file__)  # 相对路径
print(os.path.abspath(__file__))  # 绝对路径
print(os.path.dirname(os.path.abspath(__file__)))  # 返回目录去掉文件名
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)  # 添加环境变量

from day1 import login  # 跨目录调用模块
from day2 import names

login.func()  # 调用
