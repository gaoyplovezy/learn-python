#将vserach.py做成发布包，然后使用pip命令安装
#需要三个文件：setup.py、README.txt、发布文件.py
from setuptools import setup

setup(
	name="vsearch",
	version='1.0',
	description='创建的字符串集合包含函数',
	author='gaoyp',
	author_email='xxx',
	url='',
	py_modules=['vsearch']
	)