# 定义函数,进行文档说明
def add(x, y):
    # :param 参数:
    # :return 返回值:
    """
    add函数可以接收2个参数,进行2个数字相加的功能
    :param x: 形参x表示相加的其中一个数字
    :param y: 形参y表示相加的另一个数字
    :return: 返回值是两个数相加的结果
    """
    result = x + y
    print(f"2个数相加的结果是:{result}")
    return result


add(5, 6)
