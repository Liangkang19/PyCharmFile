# 丰富的else语句
# while-else的搭配

while 条件1:
    if 条件2:
        执行体1
        break
    执行体2
else:            #else后的执行体3，只在while循环结束后才被执行
    执行体3      #若中间执行break语句跳出循环，则else语句后内容不执行

# try-else的搭配
try:
    int('abc')                        
except ValueError as reason:
    print('赋值出错！错误原因：'+ str(reason))
else:                 # 若expect部分未执行，则执行else后的语句
    print('无异常！')

# 简洁的with语句

    


