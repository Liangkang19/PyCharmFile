# 用辗转相除法求两个数的最小公因数
def f1(x,y):
    while y:
        if x > y:
            temp = x % y
            x = y
            y = temp
        else:
            x,y = y,x
            temp = x % y
            x = y
            y = temp
    return x

           
           
      


