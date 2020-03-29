from DbCm import oracleDbCm

with oracleDbCm('newcmis_dev','newcmis_dev','192.168.251.248','1521','orcl.cmis') as cursor:
	cursor.execute("select * from s_usr")
	row = cursor.fetchall()
	for f in row:
		print(f)