print('-------------猜数小游戏--------------\n')
import random
secret = random.randint(1,10)
temp = input("猜一下小甲鱼现在心里想的是哪个数字:")
i=0
while i<3:    
    guess = int(temp)
    if guess == secret:
        print("卧槽，你是小甲鱼心里蛆虫吗？！")
        print("哼，猜中了也没有奖励！")
        i=3
    else:
        if guess > secret:
            print("哥，大了大了！！")
        else:
            print('哥，小啦小啦~~')
        i=i+1
        temp = input("请重新猜一个数:")
print("游戏结束，不玩啦~")
    
        
    
    
