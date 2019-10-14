# 匿名函数：lambda
lambda x,y : 2 + x + y                #lambda函数的定义格式
g = lambda x,y : 2 + x + y            #lambda函数的调用方法
g(5,6)

# 过滤器函数 filter()
filter(None,[1,0,True,False])         #将非True的内容过滤掉
list(filter(None,[1,0,True,False]))   #输出：[1, True]

def odd(x):
    return x % 2                      #x为奇数时：返回0，x为偶数时：返回1
temp = range(10)                      #将temp中的元素代入odd函数中运行
list(filter(odd,temp))                #若odd返回1，则该元素被筛选出来，否则该元素被过滤
                                      #输出：[1, 3, 5, 7, 9]
list(filter(lambda x:x%2,range(10)))  #使用lambda函数实现相同功能
# 注意filter中的第一个参数为函数时，调用时只需要填：odd 不需要加括号

# 映射函数：map()
list(map(lambda x:x+2,range(10)))     #将第二个参数的元素放入第一个参数中迭代，并输出所有的返回值
