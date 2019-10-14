# 继承机制
class Parent:
    def hello(self):
        print('正在调用父类的函数...')


class Child(Parent):               # 子类继承父类的格式
    pass


p = Parent()
print(p.hello())
c = Child()
print(c.hello())
