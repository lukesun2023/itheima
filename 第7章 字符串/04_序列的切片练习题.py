my_str = "万过月薪,员序程马黑来,nohtyp学"

# 要求：通过任何方式得到“黑马程序员”
# 切片倒序直接取出
print(my_str[9:4:-1])

# 切片，然后从头到尾切片倒序
new_my_str = my_str[5:10]
new_my_str = new_my_str[::-1]

# split分割，replace替换“来”为空,倒序字符串
new_my_str = my_str.split(",")
new_my_str = new_my_str[1].replace("来", "")
new_my_str = new_my_str[::-1]
print(new_my_str)