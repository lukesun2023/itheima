# 函数作为参数传递的实例:
def test_func(compute):
    result = compute(1, 2)
    print(result)


def compute(x, y):
    return x + y


test_func(compute)
# 将函数作为参数传递是一种计算逻辑的传递,而非数据的传递
# 需要计算的数据是确定,不确定的是计算逻辑
# 以数据作为参数传递时,计算逻辑是确定的而计算过程中的数据是不确定的(通过参数确定)


# 定义一个函数,接收另一个函数作为传入参数
def test_func(compute):
    result = compute(1, 2)
    print(type(compute))
    print(result)


# 定义一个函数,准备作为参数传入另一个函数
def compute(x, y):
    return x + y


# 调用,并传入函数
test_func(compute)


# 总结:
# 1.函数本身可以作为参数,传入另一个函数中使用
# 2.将函数传入的作用在于:传入计算逻辑,而非传入数据
