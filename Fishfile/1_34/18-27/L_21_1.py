lambda x,y=3:x*y

def f1(x):
    if x%2:
        return x
    else:
        return None


#3.将100以内3的倍数输出
list(filter(lambda x:not(x%3),range(1,100)))
list(map(lambda x,y : [x,y],[1,3,5,7,9],[2,4,6,8,10]))
#输出：[[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
def make1(n):
    return lambda s : s * n
dou = make1(2)
print(dou(8))
print(dou('F'))
