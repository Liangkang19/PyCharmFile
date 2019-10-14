# self :指针


class Ball:

    def setname(self, name):
        self.name = name

    def kick(self):
        print('我是%s，谁踢我>>>' % self.name)


a = Ball()             # 类调用后 --> 生成对象a
a.setname('篮球')      # 往对象a中添加参数
b = Ball()             # 类调用后 --> 生成对象a
b.setname('足球')      # 往对象a中添加参数
a.kick()               # 则对象a和b中相同函数输出不同的值
b.kick()

# 面向对象的编程
# __init__(self)


class Balls:

    def __init__(self, name):
        self.name = name

    def kick(self):
        print('我是%s，谁踢我>>>' % self.name)


c = Balls('土豆')    # 调用类生成对象c时，可同时导入参数
c.kick()

# 公有和私有


class Person:
    name = '老四'


p = Person()    # 生成对象
print(p.name)   # 此时name为公有变量，可以使用p.name 进行访问


class Person2:
    __name = '阿峰'     # 变量名前加__,变为私有变量 本质上：_类名__变量名

    def getname(self):
        return self.__name


p1 = Person2()          # 此时无法使用p1.__name方式访问该变量
print(p1.getname())     # 可以通过class中的内部函数进行访问











