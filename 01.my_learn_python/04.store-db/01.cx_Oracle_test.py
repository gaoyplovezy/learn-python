import cx_Oracle#引用模块cx_Oracle
 
#conn = cx_Oracle.connect('ncmis_poc/ncmis_poc@192.168.253.128:1521/orcl')
conn = cx_Oracle.connect('newcmis_dev/newcmis_dev@192.168.251.248:1521/orcl.cmis')#连接数据库
cur = conn.cursor() #获取cursor
cur.execute("select USR_NAME from S_USR")#使用cursor进行各种操作
#row =cur.fetchone() #返回元祖,fetchone只返回一条
row =cur.fetchall() #返回元祖,fetchall返回全部
 
for f in row:
    print(f)

conn.commit()
cur.close()#关闭cursor
conn.close()
