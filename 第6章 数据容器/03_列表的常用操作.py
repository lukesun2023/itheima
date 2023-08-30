# 列表的一系列操作包括：插入元素、删除元素、清空列表、修改列表、统计元素个数等等
# 这些功能都是通过列表的方法来实现的
# 函数是直接被定义的
# 方法是被定义为class(类)的成员的函数
# 函数是通过函数名直接调用的
# 方法是通过'类名.方法'的方式调用的


my_list = ["itheima", "itcast", "python"]
# 1.1 查找某元素在列表中的索引
# 语法：列表.index(元素)
# 作用：返回值为元素值的索引
print(my_list.index("itheima"))
# .index()方法返回值的数据类型是
print(type(my_list.index("itheima")))
# 尝试一个不存在的内容
# 报错，提示不在列表中
# print(my_list.index("hello"))

# 1.2 修改列表中的指定元素
# 语法：列表[索引] = 值
# 例如：修改my_list中的元素为传智教育
my_list[0] = "传智教育"
print(my_list)

# 1.3 在指定的下标位置传入指定的数据
# 语法：列表.insert(要插入的下标位置, 要插入的元素)
my_list.insert(1, "best")
print(my_list)

# 1.3 追加元素
# 语法：列表.append(要插入的元素)
my_list.append("黑马程序员")
print(f"列表在追加了元素后，结果是{my_list}")

# 1.4 追加一批元素
# 语法：列表.extend(其他的数据容器)
my_list2 = [1, 2, 3]
my_list.extend(my_list2)
print(f"列表在追加了一个新的容器后的结果是：{my_list}")


# 重新给列表赋值
my_list = ["itheima", "itcast", "python"]

# 方式1：del 列表[下标]
del my_list[1]
print(my_list)

# 方式2：列表.pop[下标]
# 作用：通过pop取出例表中指定元素
my_list = ["itheima", "itcast", "python"]
element = my_list.pop(2)
print(my_list)
print(element)


my_list = ["itheima", "itcast", "python"]
# 方式3：列表.remove(需要删除的元素值)
# 作用：删除值为指定值的第一个元素
my_list.remove("itheima")
print(my_list)

# 清空列表
# 语法：列表.clear()
my_list.clear()
print(f"列表被清空了！{my_list}")

my_list = ["itheima", "itcast", "python"]
# 统计某元素在列表中的数量
# 语法：列表.count(元素)
count = my_list.count("itheima")
print(f"列表中，itheima的数量是{count}")

my_list = ["itheima", "itcast", "python"]
# 统计列表内有多少元素
# 语法：len(列表)
count = len(my_list)
print(f"列表中的元素数量总共有{count}")
