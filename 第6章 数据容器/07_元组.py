# 列表与元组的最大区别在于列表可以被修改,而元组不可以被修改
# 元组可以被认为是一个只读的list
# 元组的定义语法:
# 变量名 = (元素, 元素, 元素)
# 元组与列表在定义时的区别在于列表用[]定义,而元组使用()定义

# 定义元组,元组英文名字为tuple,该单词为关键字,所以不能在定义中使用
t1 = (1, "Hello", True)
t2 = ()
t3 = tuple()
print(f"t1的类型是:{type(t1)},内容是:{t1}")
print(f"t2的类型是:{type(t2)},内容是:{t2}")
print(f"t3的类型是:{type(t3)},内容是:{t3}")

# 定义单个元素的元组
# NOTE 如果元组中只有一个元素,必须使用',空格'的形式,否则不会被认定为元组,而是单个元素的数据类型
t4 = ("hello", )
print(f"t4的类型是:{type(t4)},t4的内容是:{t4}")

# 元组的数据类型是不受限的,所以元组可以嵌套元组
t5 = ((1, 2, 3), (4, 5, 6))
print(f"t5的类型是{type(t5)},内容是:{t5}")

# 下标索引取出元组的内容
print(t5[1][2])


# NOTE 由于元组不可修改的特性,所以元组的常用操作一般只有index,count,len,使用方法与列表完全一致
# 元组的操作:index查找方法(与列表完全一样)
t6 = ("传智教育", "黑马程序员", "Python")
index = t6.index("黑马程序员")
print(f"在元组t6中查找黑马程序的下标是:{index}")

# 元组的操作:count统计方法
t7 = ("传智教育", "黑马程序员", "黑马程序员", "Python")
num = t7.count("黑马程序员")
print(f"在元组t7中统计黑马程序员的数量有:{num}")

# 元组的操作:len函数统计元组元素的数量
t8 = ("传智教育", "黑马程序员", "黑马程序员", "Python")
num = len(t8)
print(f"t8元组中的元素有{num}个")

# 元组的遍历:while
index = 0
while index < len(t8):
    print(f"元组的元素有:{t8[index]}")
    index += 1

# 元组的遍历:for
for element in t8:
    print(f"元组的元素有:{element}")


# NOTE 元组操作的注意事项
# t8[0] = "itcast"
# 上面的代码会报错,元组的元素是不能修改的

# NOTE 特例:元组中列表的元素是可以修改的
t9 = (1, 2, ["itheima", "itcast"])
print(f"t9的内容是:{t9}")
t9[2][0] = "黑马程序员"
print(f"t9被修改后的内容是:{t9}")
