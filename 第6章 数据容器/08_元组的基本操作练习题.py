information = ('周杰伦', 11, ["football", "music"])
# 使用index方法获得学生年龄的下标
print(f"年龄的下标是:{information.index(11)}")

# 使用索引获得对应位置的元素值
print(f"学生的姓名是:{information[0]}")

# 删除爱好中的football
del information[2][0]

# 增加爱好到list内
information[2].append('AV')
print(f"增加元素的列表之后的元组为:{information}")
