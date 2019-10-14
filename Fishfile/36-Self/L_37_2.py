# 编写一个游戏程序，其要求如下：
# (1)游戏场景的范围是(x,y)平面：0<=x<=10,0<=y<=10
# (2)游戏生成1个华农和10只竹鼠
# (3)其移动方向是随机的，华农可以移动1格或者2格(随机)，竹鼠可以移动1格
# (4)当移动到场景边缘时，自动反方向移动
# (5)华农初始体力为100(上限)，每移动一次，体力-1
# (6)竹鼠不计算体力
# (7)当华农和竹鼠坐标重叠时，华农吃掉竹鼠，华农体力增加20
# (8)当华农体力为0或竹鼠数量为0时，游戏结束

import random as r

legalx = [0, 10]
legaly = [0, 10]


class Huanong:
    def __init__(self):
        self.power = 100                           # 设置初始体力
        self.x = r.randint(legalx[0], legalx[1])   # 随机设置初始位置
        self.y = r.randint(legaly[0], legaly[1])

    def move(self):
        newx = self.x + r.choice([1, 2, -1, -2])   # 随机移动到任意方向
        newy = self.y + r.choice([1, 2, -1, -2])   # 随机移动1格或2格




