# 递归调用
def return1():
    return  return1()
def f1(n):
    s = 1
    for i in range(1,n+1):
        s = s * i
    return s
def fx(n):                   # 当输入实参为3，即fx(3),其运行过程如下：
    if n == 1:               # fx(3) = 3 * fx(2)    
        return 1             # fx(2) = 2 * fx(1)
    else:                    # fx(1) = 1
        return n * f2(n-1)   # 故fx(3) = 3 * fx(2) = 3 * (2 * fx(1)) = 3 * 2 * 1=6
# 递归调用的实质是：
# 1.先执行“递”操作,得到fx(n),fx(n-1),fx(n-2)......等函数的表达式
# 2.在指定条件中停止“递”操作，得到一个确定的函数值 fx(1)
# 3.再执行“归”的操作，将fx(1)的值代入fx(2)函数中，得到fx(2)的值......
#   将fx(n-1)的值代入fx(n)中，最终得到fx(n)的值
        
