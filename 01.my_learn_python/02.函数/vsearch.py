def fun_search():
    vowels = set('aeiou')
    word = input("输入待比较文本：")
    set_word = set(word)
    u = vowels.union(set_word)
    d = vowels.difference(set_word)
    i = vowels.intersection(set_word)
    print('并集：')
    for k in u:
        print(k)

   
    print('在第一个集合且不在第二个集合中：')
    for k in d:
        print(k)

    
    print('交集：')
    for k in i:
        print(k)
    return i


#第二个参数赋默认值
def fun_param(wo:str,defval:str='asdfd') -> list:
    print(list(defval))
#函数调用必须在函数定义之后
fun_param("wo",'defvalue')
