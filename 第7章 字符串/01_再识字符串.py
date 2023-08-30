# 字符串也可以看做是数据容器

my_str = "itheima and itcast"

# 通过下标索引取值
value1 = my_str[2]
value2 = my_str[-16]
print(f"从字符串{my_str}取下标为2的元素为{value1}")
print(f"从字符串{my_str}取下标为-12的元素为{value2}")

# 字符串是不可修改的
# index方法
value = my_str.index("and")
print(f"字符串{my_str}中查找and元素,起始下标为:{value}")


# 字符串的替换
# 语法:字符串.replace(字符串1, 字符串2)
# 功能:将字符串内的全部字符串1替换为字符串2
# NOTE 不是修改字符串,而是得到了一个新的字符串
new_my_str = my_str.replace("it", "程序")
print(f"将字符串{my_str},进行替换后得到:{new_my_str}")


# 字符串的分隔
# 语法:字符串.split(分隔字符串)
# 功能:按照指定的分隔符字符串,将字符串划分为多个字符串,并存入列表对象中
# NOTE 字符串本身不变,而是得到了一个新的字符串
my_str = "hello python itheima itcast"
my_str_list = my_str.split(" ")
print(f"将字符串{my_str}进行spblit切分后得到:{my_str_list},类型是:{type(my_str_list)}")


# 字符串的规整操作(去前后空格)
# 语法:字符串.strip()
my_str = " itheima and itcast "
print(my_str.strip())

# 字符串的规整操作(去前后指定字符串)
# 语法:字符串.trip(字符串)
my_str = "12itheima and itcast21"
print(my_str.strip("12"))
# NOTE 传入"12"其实就是"1"和"2"都会移除,是按照单个字符


# 统计字符串中某字符串出现的次数
my_str = "itheima and itcast"
count = my_str.count("it")
print(f"字符串{my_str}中it出现的次数是:{count}")


# 统计字符串的长度
num = len(my_str)
print(f"字符串{my_str}的长度是:{num}")
