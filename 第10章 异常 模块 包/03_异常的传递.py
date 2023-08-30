# 异常具有传递性

# 定义一个出现异常的函数
def func1():
    print("func1 开始执行")
    num = 1 / 0
    print("func1 结束执行")


# 定义一个无异常的函数,调用上面的方法
def func2():
    print("func2 开始执行")
    func1()
    print("func2 结束执行")


def main():
    try:
        func2()
    except Exception as e:
        print(f"出现异常了,异常的信息是:{e}")


main()

# NOTE main函数可以捕捉到异常,而有问题的是func1,由此可见,异常是具备传递性的.只要函数之间有调用关系,调用了异常函数的函数也是可以捕获异常的.
