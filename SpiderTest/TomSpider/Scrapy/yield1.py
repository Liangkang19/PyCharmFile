# 生成器yield的用法


def gen(n):
    for i in range(n):
        yield i**2


for t in gen(5):
    print(t, ' ', end='')


