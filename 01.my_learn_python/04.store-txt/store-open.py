
'''
1、open来打开一个文件，如果一切顺利，open会返回一个流
2、'a'表示：采用追加模式打开这个文件
'''
todos = open('todos.txt','a')
#在print中打印多个值时，可以使用sep指定分隔符，默认是空格分隔
print('Put out the trash','分隔我',file=todos,sep='|')
print('Feed the cat',file=todos)
print('Prepare tax return',file=todos)
#关闭文件流，若不关闭则容易造成写入的数据丢失
todos.close()

#打开文件，并读取每一行，不加参数则表示只读模式打开
tasks = open('todos.txt')
for line in tasks:
	print(line)
'''
end=''表示：抑制print追加换行符的默认行为
for line in tasks:
	print(line,end='')
'''
#虽然只是从文件中读取数据，但还是建议关闭
tasks.close()