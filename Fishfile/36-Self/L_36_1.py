class Rectangle:
    x = 5
    y = 4

    def setrect(self):
        print('请输入矩形的长和宽:')
        self.x = int(input('长:'))
        self.y = int(input('宽:'))

    def getrect(self):
        print('矩形的长：%d  宽：%d' % (self.x, self.y))

    def getarea(self):
        a = self.x * self.y
        return a


rect = Rectangle()    # 调用类 --> 生成对象rect
rect.setrect()        # 对象中的函数调用(若含有除self之外的参数，可输入参数)
rect.getrect()
print(rect.getarea())
