#函数：1)计算所有参数的和乘以基数(base=3)的结果
#      2)若最后的参数为5，则令(base=5),计算所有参数的和乘以基数(base=5)的结果
def mfun(*param,base=3):
    sum1 = 0
    for each in param:
        sum1 = sum1 + each
    sum1 = sum1*base
    print(sum1)

# mfun(1,2,3,4,5,base=5)


#函数：1)计算所有参数的和乘以基数(base=3)的结果
#      2)若最后的参数为5，则令(base=5),且基数不参与求和运算。
def test(*params):    
    k=len(params)
    if params[(k-1)] == 5:
        base=5
        k=k-1
    else:
        base = 3
    sum1 = 0
    i=0
    while k:
        sum1 = sum1+params[i]
        i=i+1
        k=k-1 
    sum1=sum1*base
    return sum1

# 求水仙花数

def Nar():
    for each in range(100,1000):
        temp = each
        sum1 = 0
        while temp:
            sum1 = sum1+(temp%10)**3
            temp = temp//10
        if sum1 == each:
            print(each,end='\t')
   
 
