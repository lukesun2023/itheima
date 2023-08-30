# 列表的遍历-while循环
"""
index = 0
while index < len(列表)
    元素 = 列表[index]
    对元素进行处理
    index += 1
"""


# 使用while循环遍历列表中的元素
def list_while_func():
    """
    使用while循环遍历列表中的元素
    :return: None
    """
    my_list = ["传智教育", "黑马程序", "Python"]
    # 循环控制变量通过下标索引来控制，默认0
    # 每一次循环将下标+1
    # 循环控制条件：下标索引变量 < 列表的元素数量

    # 定义一个变量来标记列表的下标
    index = 0
    while index < len(my_list):
        # 通过index变量取出对应下标的元素
        element = my_list[index]
        print(f"列表的元素：{element}")
        # 将循环变量index每次循环都加1
        index += 1


list_while_func()


# 使用for循环对列表进行遍历
"""
for 临时变量 in 数据容器:
    对临时变量进行相应的处理
"""


def list_for_func():
    my_list = [1, 2, 3, 4, 5]
    for element in my_list:
        print(f"列表的元素有:{element}")


list_for_func()
