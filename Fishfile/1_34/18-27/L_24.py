# 汉诺塔的递归调用
def Hanoi(n,x='x',y='y',z='z'):
    '使用递归调用解决汉诺塔问题'
    if n == 1:
        print(x,'-->',z)
    else:
        Hanoi(n-1,x,z,y)   #将前n-1个盘子从x移动到y
        print(x,'-->',z)   #将最底下的最大盘子从x移动到z
        Hanoi(n-1,y,x,z)   #将n-1个盘子从y移动到z上
