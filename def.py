import time


# 参数
def funname(a, b, *args, d=2):
    print(a)
    print(b)
    print(*args)
    print(d)


funname(1, 2, 3, 4, 5, 6, 7)


# 闭包
def outer():
    x = 1

    def inner():  # 闭包
        y = x + 1

    return inner


# 装饰器
def cal_time(fn):
    def inner():
        start = time.time()
        fn()
        end = time.time()
        print('代码耗时:', end - start)

    return inner


@cal_time  # 1、自动调用函数 cal_time 2、并把被装饰的函数(装饰器下方的)传给fn
def zsqdemo():
    x = 0
    for i in range(1, 10000000):
        x += i
    print(x)

# 3、在次调用被装饰的函数zsqdemo时,这个函数已经改变成 cal_time return的函数了
zsqdemo()
