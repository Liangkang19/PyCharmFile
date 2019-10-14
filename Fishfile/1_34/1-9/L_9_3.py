for i in range(100,1000):
    sum = 0
    temp = i
    while temp:
        sum = sum + (temp%10)**3
        temp = temp // 10    # 使用地板除法
    if sum == i:
        print(i)
