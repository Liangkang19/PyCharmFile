# 使用递归调用将十进制转二进制
def Ten(x):
    result = ''
    if x:
        result = Ten(x//2)
        return result + str(x%2)
    else:
        return result

# 使用递归调用将一个数的个位，十位，百位等输出

re = []
def Digits(x):
    if x > 0:
        re.insert(0,x%10)
        Digits(x//10)
# 使用递归求年龄

def age(n):
    if n == 1:
        return 10
    else:
        return age(n-1)+2
print('第5个人是%d岁'% age(5))
    

    
