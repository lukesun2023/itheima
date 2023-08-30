def list_for_func(pending_list):
    """
    使用for循环，取出传入列表中所有偶数元素组成一个新的列表
    :return: 元素值为偶数的元素构成的新列表
    """
    processed_list = []
    for element in pending_list:
        if element % 2 == 0:
            processed_list.append(element)
    return processed_list


def list_while_func(pending_list):
    """
    使用while循环，取出传入列表中所有偶数元素组成一个新的列表
    :return: 元素值为偶数的元素构成的新列表
    """
    index = 0
    processed_list = []
    while index < len(pending_list):
        if pending_list[index] % 2 == 0:
            processed_list.append(pending_list[index])
        index += 1
    return processed_list


pending_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
processed_list = list_for_func(pending_list)
print(f"通过for循环，从列表：{pending_list}中取出偶数，组成新列表:{processed_list}")

processed_list = list_while_func(pending_list)
print(f"通过while循环，从列表：{pending_list}中取出偶数，组成新列表:{processed_list}")
