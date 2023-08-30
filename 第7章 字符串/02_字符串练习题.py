my_str = "itheima itcast boxuegu"

# 统计字符串中有多少个it
count = my_str.count("it")
print(f"字符串{my_str}中,一共有{count}个'it'")

# 将字符串内的空格全部替换为字符:"|"
my_str = "itheima itcast boxuegu"
new_my_str = my_str.replace(" ", "|")
print(f"字符串替换的结果为:{new_my_str}")

# 按照"|"进行字符串分割,得到列表
new_my_str = new_my_str.split("|")
print(f"处理后的列表为:{new_my_str}")
