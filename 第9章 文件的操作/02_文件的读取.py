# 文件操作包括哪些内容:
# 打开\关闭\读\写等操作
# python操作文件的步骤:
# 1.打开文件
# 2.读写文件
# 3.关闭文件


# open()打开函数
# 语法:open(name, mode, encoding)
# name:要打开的文件名的字符串(可以包含文件所在的具体路径)
# mode:设置打开文件的模式:只读\写入\追加等
# encoding:编码格式(推荐使用utf-8)


# 打开文件
f = open(r"D:\python\itheima\test\test.txt", "r", encoding='UTF-8')
print(type(f))

# read()方法:
# 语法:文件对象.read(num)
# num表示从文件中读取的数据的长度(单位是字节),如果没有传入num,那么表示读取文件中的所有数据
# print(f"读取10个字节的方法:{f.read(10)}")
# print(f"read方法读取全部内容的结果是{f.read()}")


# readline()方法:
# 作用:可以按照行的方式把整个文件中的内容进行一次性读取,并且返回的是一个列表,其中每一行的数据为一个元素
# lines = f.readlines()
# print(f"lines对象的类型:{type(lines)}")
# print(f"lines对象的内容是:{lines}")

# NOTE 文件操作的read相关指令,是有类似指针存在的,调用read方法的时候,下一个read指令会续接上一个read指令指针的位置

# 读取文件 readline()
# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()
# print(f"第一行数据是:{line1}")
# print(f"第二行数据是:{line2}")
# print(f"第三行数据是:{line3}")


# 采用for循环读取文件的行
for line in f:
    print(f"每一行数据是:{line}")


# 关闭文件的方法:
# 语法:f.close()
f.close()


# with open 语法操作文件
with open(r"D:\python\itheima\test\test.txt", "r", encoding='UTF-8') as f:
    for line in f:
        print(f"每一行数据是:{line}")
# NOTE with open与open方法的区别是with open在执行完:后面的指令后,会自动关闭文件
