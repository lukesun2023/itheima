# 读取文件,并且在文件中查找制定的内容
# 方法1：先用read方法读取文件，然后使用count方法查找并对出现的次数计数
# 方法2：可以使用f.readlines()
# 文件的写操作与读操作的步骤相似:1.打开文件 2.写入文件 3.关闭文件
# NOTE 在写入操作完成后,多了一步使用f.flush方法刷新内容
# 写入操作执行后,没有立即写入文件中,而是在内存中更改了相关内容,只有调用了flush方法或者close方法关闭文件时,才会将变更的数据写入文件
# 实例:
import time

f = open(r"D:\python\itheima\test.txt", "w", encoding="UTF-8")
# write写入
f.write("Hello world!!!")
# flush刷新
f.flush()
# clsoe
f.close()

# NOTE 文件存在会把文件清空,然后写入内容,文件不存在,创建新文件,写入内容

# 总结
# 写入文件使用open的"w"模式
