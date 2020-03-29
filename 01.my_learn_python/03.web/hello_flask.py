from flask import Flask


"""
1、创建一个Flask类型的对象
2、__name__，注意：是双下划线，不是一个
3、__name__值由python解释器维护，任何使用这个值时，它会设置为当前活动模块的名字
"""
app = Flask(__name__)

#@前缀表示修饰符，这里是一个函数修饰符，可以调整一个已有函数的行为（而不用修改函数的代码）
@app.route('/hello')
def hell() -> str:
	return 'hello world from flask'


@app.route('/hell')
def fun_hell() ->str:
	return 'THis is fun_hell'

#让web应用开始运行
app.run()