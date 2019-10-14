# 十进制转二进制

def f2(x):
    list1 = []
    str1 = ''
    while x:
        t1 = x % 2
        x = x // 2
        list1.append(t1)
    while list1:
        str1 = str1 + str(list1.pop())
    return str1
    
        
     
