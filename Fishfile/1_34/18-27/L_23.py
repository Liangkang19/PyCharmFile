# 裴波那契数列的递归实现
def Pei1(n):
    '使用迭代法计算裴波那契数列的和'
    s1 = 1
    s2 = 1
    s3 = 1
    if n <= 2:
        return s3
    else:
        for i in range(3,n+1):
            s3 = s1 + s2
            s1 = s2
            s2 = s3
        return s3
def Pei2(n):
    '使用递归法计算裴波那契数列的和'
    if n <= 2:
        return 1
    else:
        return Pei2(n-1) + Pei2(n-2)
    
            
