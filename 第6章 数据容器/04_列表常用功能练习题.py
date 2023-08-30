# 定义一个列表，并用变量接收它
age = [21, 25, 21, 23, 22, 20]

# 追加一个数字31到列表的尾部
age.append(31)
print(age)

# 追加一个新列表[29, 33, 30],到列表的尾部
age1 = [29, 33, 30]
age.extend(age1)
print(age)

# 取出第一个元素
extracted_element = age.pop(0)
print(extracted_element)
print(age)

# 取出最后一个元素
extracted_element = age.pop(-1)
print(extracted_element)
print(age)

# 查找元素31在列表中的下标位置
index_number = age.index(31)
print(index_number)
