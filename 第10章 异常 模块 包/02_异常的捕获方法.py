# 学习目标
# 1.知道为什么要捕获异常
# 2.掌握捕获异常的语法格式

# 程序遇到bug之后可能出现的两种情况:
# 1.整个程序因为一个BUG停止运行
# 2.对BUG进行提醒,整个程序继续运行----捕获异常

# 基本语法:
# try:
#   可能发生错误的代码
# except:
# 如果出现异常执行的代码

# 基本捕获语法(try和except成对使用):
try:
    f = open("linux.txt", "r", encoding="UTF-8")
except:
    print("出现异常了,因为文件不存在,我将open的模式改为'w'模式!")
    f = open("linxu.txt", "w", encoding="UTF-8")

# 捕获指定的异常:
try:
    print(name)
except NameError as e:
    print("出现了变量未定义的异常")

try:
    print(name)
except (NameError, ZeroDivisionError) as e:
    print("出现了变量未定义或者除0异常!")

# 捕获所有的异常类型:
try:
    1/0
except Exception as e:
    print("出现异常了!")
