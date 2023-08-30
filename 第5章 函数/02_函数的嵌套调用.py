"""
演示嵌套调用函数
"""


# 定义函数func_b
def func_b():
    print("123")


# 定义函数func_a,并在其内部调用func_b
def func_a():
    """
    func_a调用了func_b
    :return: 返回值为NoneType
    """
    print("---1---")

    # 嵌套调用
    func_b()

    print("---3---")


# 调用函数func_a
func_a
func_b
