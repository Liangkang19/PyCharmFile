# 属性(静态变量)+方法(动态函数) = 对象
# 类: class
# 封装：对外部隐藏对象的工作细节


class Laosi:
    # 类的属性
    color = 'yellow'
    weight = 70
    legs = 2
    words = '大家好，我是老四'

    # 类的方法
    def eat(self):
        print('这只竹鼠好像中暑了!')

    def run(self):
        print('这只鸡跑得好快！')


tt = Laosi()    # 类调用后 --> 生成对象tt
tt.eat()        # 对象的使用

# 继承：子类自动共享父类之间数据和方法的机制


class Mylist1(list):
    pass


list1 = Mylist1()    # 类调用后 --> 生成对象list1
list1.append(5)      # 可以继承使用list相关的操作

# 多态：不同对象调用相同名称的函数，输出相同或不同的功能


class A:
    def fun1(self):
        print('我是小A！')


class B:
    def fun1(self):
        print('我是小B！')


a = A()
b = B()      # 类调用后 --> 生成对象a和b
a.fun1()     # 多态：即不同对象调用相同名称的fun1()函数，所实现的功能不同
b.fun1()







