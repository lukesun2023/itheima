# 几种数据容器的特点:
# 列表可修改,支持重复元素且有序
# 元组,字符串不可修改,支持重复元素且有序
# 集合,最主要的特点是不支持重复元素(相当于自带去重功能),并且内容无序

# NOTE 几种数据容器的定义方式:
# 列表: []
# 元组:()
# 字符串:""
# 元组:{}


# 定义集合
# 通过这个定义可以看到两个集合的两个特点：
# 1.不能重复（具有自动去重的功能）
# 2.内容无序
my_set = {"传智教育", "黑马程序员", "itheima", "传智教育",
          "黑马程序员", "itheima", "传智教育", "黑马程序员", "itheima"}
my_set_empty = set()
print(f"my_seet的内容是:{my_set},类型是：{type(my_set)}")
print(f"my_set_empty的内容是:{my_set_empty},类型是:{type(my_set_empty)}")

# 添加新元素
# 语法：集合.add(元素)
my_set.add("python")
print(f"my_set添加元素后结果是:{my_set}")

# 移除元素
# 语法：集合.remove(元素)
my_set.remove("黑马程序员")
print(f"my_set移除'黑马程序员'的结果是:{my_set}")

# 随机取出一个元素
# 语法：集合.pop()
element = my_set.pop()
print(f"my_set通过pop方法取出的元素是:{element}")
print(f"取出元素后，my_set集合：{my_set}")

# 清空集合
# 语法：集合.clear()
my_set.clear()
print(f"集合使用clear清空后变成：{my_set}")

# 取出两个集合的茶几
# 语法：集合1.difference(集合2)
# 功能：取出集合1和集合2的差集（集合1有而集合2没有的元素）
# 结果：得到一个新集合，集合1和集合2不变
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set3 = set1.difference(set2)
print(f"取差集后的集合1为:{set1}")
print(f"取差集后的集合2为:{set2}")
print(f"取差集后的集合3为:{set3}")

# 消除两个集合的差集
# 语法：集合1.difference_update(集合2)
# 功能：对比集合1和集合2，在集合1内，删除和集合2相同的元素
# 结果：集合1被修改，集合2不变
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set1.difference_update(set2)
print(f"消除差集后的集合1为:{set1}")
print(f"消除差集后的集合2为:{set2}")

# 2个集合合并成1个
# 语法：集合1.union(集合2)
# 功能：将集合1和集合2组合成新集合
# 结果：得到心机和，集合1和集合2不变
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set3 = set1.union(set2)
print(f"2个集合合并的结果：{set3}")
print(f"合并后集合1:{set1}")
print(f"合并后集合2:{set2}")

# 统计集合元素数量len()
set = {1, 2, 3, 4, 5}
num = len(set1)
print(f"集合内的元素数量有:{num}个")

# 集合的遍历
# 因为集合是无序的没有下标索引，所以无法使用while循环遍历
# 可以用for循环进行遍历
set1 = {1, 2, 3, 4, 5}
for element in set1:
    print(f"集合的元素有:{element}")
