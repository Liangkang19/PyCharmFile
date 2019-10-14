# 0：按照要求定义一个游乐园门票的类，并计算2个成人和1个小孩的平日票价
# 平日票价100元
# 周末票价为平日票价的120%
# 儿童半票


class Ticket():
    def __init__(self, weenkend=False, child=False):
        self.ticket = 100
        if weenkend:
            self.rate = 1.2
        else:
            self.rate = 1
        if child:
            self.discount = 0.5
        else:
            self.discount = 1

    def countprice(self, num):
        return self.ticket * self.rate * self.discount * num


adult = Ticket()                     # 建立对象1
child = Ticket(child=True)           # 建立对象2
money = adult.countprice(2) + child.countprice(1)  # 调用对象1,2中的函数

# 同一个类，分成两个不同的对象(成人和儿童)，则不同对象中的参数值不同
# 所以调用(成人或者儿童)对象时，可以得出不同的结果
