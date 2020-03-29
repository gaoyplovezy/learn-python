import cx_Oracle
'''
所有变量的使用必须前面加self.
'''
class oracleDbCm:
	def __init__(self,user:str,passwd:str,ip:str,port:str,sid:str) ->None:
		self.user = user
		self.passwd = passwd
		self.ip = ip
		self.port = port
		self.sid = sid

	def __enter__(self) ->object:
		url = self.user+"/"+self.passwd+"@"+self.ip+":"+self.port+"/"+self.sid
		print(url)
		self.conn = cx_Oracle.connect(url)#连接数据库
		self.cur = self.conn.cursor() #获取cursor
		return self.cur

	'''
	1、dunder exit会处理wiht代码组中可能出现的任何异常，如果出了问题，解释器会通知__exit__，向这个方法传递三个参数：exc_type,exc_value,ext_trace
	'''
	def __exit__(self,exc_type,exc_value,ext_trace) ->None:
		self.conn.commit()
		self.cur.close()#关闭cursor
		self.conn.close()

