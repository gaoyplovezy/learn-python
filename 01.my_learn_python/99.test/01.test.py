'''
判断字段区别
'''
import os
#在new不在old
def inNewNotOld(newName,oldName):
	new_l = []
	old_l = []
	res_l = ["在"+newName+"不在"+oldName+":"]
	with open(newName) as new:
		'''
		用readlines()取出来后，带有\n，需要手工处理一下
		new_l = new.readlines()
		PS：有没有好办法处理呢？
		'''
		for n in new:
			new_l.append(n.replace('\n',''))

	with open(oldName) as old:
		for o in old:
			old_l.append(o.replace('\n',''))


	for nl in new_l:
		if nl not in old_l:
			res_l.append(nl)


	return res_l
				

#在old不在new
def inOldNotNew(newName,oldName):
	new_l = []
	old_l = []
	res_l = ["在"+oldName+"不在"+newName+":"]
	with open(newName) as new:
		for n in new:
			new_l.append(n.replace('\n',''))

	with open(oldName) as old:
		for o in old:
			old_l.append(o.replace('\n',''))


	for ol in old_l:
		if ol not in new_l:
			res_l.append(ol)


	return res_l

def outFile():
	table = ['P_LOAN_MTD','P_LOAN_MTD_DTL','P_LOAN_MTD_PHASE']
	res = []
	os.remove('resFile.txt')
	with open('resFile.txt','a+') as data:
		for t in table:
			res.clear()
			res = inNewNotOld(t+"_new.txt",t+"_old.txt")
			for ss in res:
				print(ss,sep="\n",file=data)
			
			res.clear()
			res =  inOldNotNew(t+"_new.txt",t+"_old.txt")
			for s in res:
				print(s,file=data)
			print("------------------",file=data)



outFile()

