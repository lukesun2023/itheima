# 函数的定义方法:
# 1.def关键字,定义带有名称的函数
# 2.通过lambda关键字,可以定义匿名函数(无名称)
# 有名称的函数,可以基于名称重复使用
# 无名称的匿名函数只能临时使用

# 匿名函数的定义语法:
# lambda 传入参数: 函数体(一行代码)
# lambda函数不用return语句,默认带有return功能


# 定义一个函数,接收其他函数输入
def test_func(compute):
    result = compute(1, 2)
    print(result)


test_func(lambda x, y: x + y)
# NOTE 不需要return语句,默认具有return功能,且只能单行,且只能使用一次


# 匿名函数的总结:
# 1.通过lambda关键字定义
# 2.定义语法:
#   lambda 传入参数: 函数体(一行代码)
# 3.注意事项:
# 代码只有一行且只能调用一次
