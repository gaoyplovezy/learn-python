#将Don't panic!转为on tap
phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

#方式1：
def method1():
	for i in range(4):
	    plist.pop()
	plist.pop(0)
	plist.remove("'")
	plist.insert(2,plist.pop(3))
	plist.extend([plist.pop(),plist.pop()])
	new_phrase = ''.join(plist)
	print(plist)
	print(new_phrase)

#方式2：列表切片
def method2():
	plist2 = plist[1:3:1]
	plist3 = plist[4:8:1]
	plist2.extend(plist3)
	plist2.insert(2,plist2.pop(3))
	plist2.extend([plist2.pop(),plist2.pop()])

	#join将一个字符串列表转换为一个字符串
	new_phrase = ''.join(plist2)
	print(new_phrase)
	oth_phrase = '|'.join(plist2)
	print(oth_phrase)

method1()