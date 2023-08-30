# list的下表索引默认是从0开始，最后一个数据的索引是列表所含元素数量-1
# 列表还可以反向索引，即列表的最后一个元素标记为-1，倒数第二个标记为-2
# 嵌套的列表也可以通过下标索引取出最内层的元素：
# 例如：name[0][1]取出名为name的列表中的0号元素中的1号元素


# 通过下表索引取出相应位置的数据
my_list = ["Tom", "Lily", "Rose"]

# 列表索引正向取出，每次+1
print(my_list[0])
print(my_list[1])
print(my_list[2])

# 列表索引反向取出，每次-1
print(my_list[-1])
print(my_list[-2])
print(my_list[-3])


# 取出嵌套列表中的元素
my_list = [[1, 2, 3], [4, 5, 6]]
print(my_list[0][0])
print(my_list[0][1])
