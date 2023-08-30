<<<<<<< HEAD
my_dict = {"周杰伦": 99, "林俊杰": 88, "张学友": 77}
# 新增元素
my_dict["张信哲"] = 66
print(f"字典经过新增元素后，结果是:{my_dict}")

# 更新元素
my_dict["周杰伦"] = 33
print(f"字典经过更新后，结果是：{my_dict}")

# 删除字典中的元素
# 语法： 字典.pop(key)
score = my_dict.pop("周杰伦")
print(f"字典中被移除了一个元素，结果:{my_dict},考试分数为:{score}")

# 删除元素
my_dict.clear()
print(f"字典被清空了，内容是:{my_dict}")

# 获取全部keys的方法
# 语法：字典.keys()
my_dict = {"周杰伦": 99, "林俊杰": 88, "张学友": 77}
keys = my_dict.keys()
print(f"字典的全部keys是:{keys}")
print(f"key的数据类型是:{keys}")

# 方式1：遍历字典
# 结合上面获取全部keys的方法
for key in keys:
    print(f"字典的key是:{key}")
    print(f"字典的value是:{my_dict[key]}")

# 方式2：直接对字典进行for循环，每一次循环直接得到Key
for key in my_dict:
    print(f"字典的key是:{key}")
    print(f"字典的value是:{my_dict[key]}")
# NOTE 字典不能用while循环，字典不支持下标索引，所以只能用for循环遍历

# 统计字典内的元素数量
num = len(my_dict)
print(f"字典中的元素数量有{num}个")
=======
# 新增字典元素
# 语法：字典[key] = value
# 结果：字典被修改，新增了元素
>>>>>>> 693aa8f25baeeef604d937fd5a2cb32c84378078
