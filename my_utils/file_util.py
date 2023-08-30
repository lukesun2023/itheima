def print_file_info(file_name: str) -> str:
    """
    功能:给定路径的文件内容输出到控制台
    :param file_name:即将读取的文件
    :return: NONE
    """
    f = None
    try:
        f = open(file_name, "r", encoding="UTF-8")
        content = f.read()
        print(f"文件的全部内容如下:{content}")
    except Exception as e:
        print(f"文件出现异常了,原因是:{e}")
    finally:
        if f:
            f.close()


def append_to_file(file_name, date):
    """
    功能:向指定文件追加内容
    :param file_name: 指定路径的文件
    :param date: 需要追加的字符串
    :return: None
    """
    f = open(file_name, "a", encoding="UTF-8")
    f.write(date)
    f.write("\n")
    f.close()


if __name__ == '__main__':
    print_file_info("D:\test.txt")
    append_to_file("d:/test_append.txt", "黑马程序员")
