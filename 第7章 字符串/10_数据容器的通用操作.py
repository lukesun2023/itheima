my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
my_str = "abcdefg"
my_set = {1, 2, 3, 4, 5}
my_dict = {"key1": 1, "key2": 2, "key3": 3, "key4": 4, "key5": 5}

# len(容器)元素个数
print(f"列表my_list的元素个数为:{len(my_list)}")
print(f"元组my_tuple的元素个数为:{len(my_tuple)}")
print(f"字符串my_str的元素个数为:{len(my_str)}")
print(f"集合my_set的元素个数为:{len(my_set)}")
print(f"字典my_dict的元素个数为:{len(my_dict)}")


# max(容器)
print(f"列表my_list的最大元素为:{max(my_list)}")
print(f"元组my_tuple的最大元素为:{max(my_tuple)}")
print(f"字符串my_str的最大元素为:{max(my_str)}")
print(f"集合my_set的最大元素为:{max(my_set)}")
print(f"字典my_dict的最大元素为:{max(my_dict)}")


# 类型转换:容器转列表
print(f"列表转列表的结果是:{list(my_list)}")
print(f"元组转列表的结果是:{list(my_tuple)}")
print(f"字符串转列表的结果是:{list(my_str)}")
print(f"集合转列表的结果是:{list(my_set)}")
print(f"字典转列表的结果是:{list(my_dict)}")


# 类型转换:容器转元组
print(f"列表转元组的结果是:{tuple(my_list)}")
print(f"元组转元组的结果是:{tuple(my_tuple)}")
print(f"字符串转元组的结果是:{tuple(my_str)}")
print(f"集合转元组的结果是:{tuple(my_set)}")
print(f"字典转元组的结果是:{tuple(my_dict)}")


# 类型转换:容器转字符串
print(f"列表转字符串的结果是:{str(my_list)}")
print(f"元组转字符串的结果是:{str(my_tuple)}")
print(f"字符串转字符串的结果是:{str(my_str)}")
print(f"集合转字符串的结果是:{str(my_set)}")
print(f"字典转字符串的结果是:{str(my_dict)}")


# 类型转换:容器转集合)
print(f"列表转集合的结果是:{set(my_list)}")
print(f"元组转集合的结果是:{set(my_tuple)}")
print(f"字符串转集合的结果是:{set(my_str)}")
print(f"集合转集合的结果是:{set(my_set)}")
print(f"字典转集合的结果是:{set(my_dict)}")

# NOTE 字典转换的时候只有转换成str的时候key和value都会存在,而其他类型的转换会丢失value


# 容器通用排序功能
# 语法:sorted(容器)
print(f"列表对象的排序结果是:{sorted(my_list)}")
print(f"元组对象的排序结果是:{sorted(my_tuple)}")
print(f"字符串对象排序的结果是:{sorted(my_str)}")
print(f"集合对象排序的结果是:{sorted(my_set)}")
print(f"字典对象排序的结果是:{sorted(my_dict)}")

# 反向排序
# 语法:sorted(容器, reverse=True)
print(f"列表对象的排序结果是:{sorted(my_list, reverse=True)}")
print(f"元组对象的排序结果是:{sorted(my_tuple, reverse=True)}")
print(f"字符串对象排序的结果是:{sorted(my_str, reverse=True)}")
print(f"集合对象排序的结果是:{sorted(my_set, reverse=True)}")
print(f"字典对象排序的结果是:{sorted(my_dict, reverse=True)}")