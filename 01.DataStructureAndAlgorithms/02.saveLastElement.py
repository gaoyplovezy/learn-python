'''
1.3 保存最后N个元素
输出匹配行以及最后检查过的N行文本
关键：
1、deque
2、yield
'''
from collections import deque
def search(lines,pattern,history=5):
    #deque()创建序列；maxlen限制队列的最大长度，当有新数据加入时，若队列已满，则自动移除最老的那条记录
    previous_lines = deque(maxlen=history) 
    for line in lines:
        if pattern in line:
            yield line,previous_lines
        previous_lines.append(line)

'''
if __name__ == '__main__'的意思是：当.py文件被直接运行时，if __name__ == '__main__'之下的代码块将被运行；当.py文件以模块形式被导入时，if __name__ == '__main__'之下的代码块不被运行。
'''
if __name__ == '__main__':
    with open('02.somefile.txt') as f:
        for line,prevlines in search(f,'redis',3):
            for pline in prevlines:
                print(pline,end='')
            print(line,end='')
            print('-'*20)
