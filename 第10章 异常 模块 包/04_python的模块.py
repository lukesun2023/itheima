# 模块是一个python文件,以.py结尾.模块能定义函数,类和变量.
# 模块的作用:工具包,把其中的内容导入拿过来用

# 模块的导入语法:
# [from 模块名] import [模块|类|变量|函数|*] [as 别名]

# import 模块名
# import 模块名1, 模块名2


# 使用import导入time模块使用sleep功能
# import time  # 导入python内置的time模块
# print("你好")
# time.sleep(5)
# print("我好")

# # 使用from导入time的sleep功能
# from time import sleep
# print("你好")
# sleep(5)
# print("我好")

# 使用*导入time模块的全部功能
# from time import *
# print("你好")
# sleep(5)
# print("我好")

# 使用as给特定功能加上别名
from time import sleep as sl
print("你好")
sl(5)
print("我好")

# 模块的导入一般都写在代码的开头部分
