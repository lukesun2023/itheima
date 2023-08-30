def str_reverse(s: str) -> str:
    """
    将字符串完成反转
    :rtype: str
    :param s: 需要被反转的字符串
    :return: 反转后的字符串
    """
    return s[::-1]


def substr(s: str, x: int, y: int) -> str:
    """
    功能是按照给定的下标完成给定字符串的切片
    :rtype: str
    :param s: 将被切片的字符串
    :param x: 切片的开始下标
    :param y: 切片的结束下标
    :return: 切片后的字符串
    """
    return s[x: y]


if __name__ == '__main__':
    print(str_reverse("abcdefg"))
    print(substr("abcdefg", 1, 3))
