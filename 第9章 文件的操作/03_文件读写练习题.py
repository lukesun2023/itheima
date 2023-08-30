# 打开文件,以读取模式打开
f = open(r".\test\word.txt", "r", encoding="UTF-8")
# 方式一:读取全部内容,通过字符串count方法统计itheima的数量
content = f.read()
count = content.count("itheima")
print(f"itheima在文件中一共出现了{count}次")
f.close()


# 方式2:读取文件,一行的查找
f = open(r".\test\word.txt", "r", encoding="UTF-8")
count = 0
for line in f:
    # strip方法取出开头和结尾的空格和换行符
    line = line.strip()
    words = line.split(" ")
    for word in words:
        if word == 'itheima':
            count += 1
print(f"itheima出现的次数是:{count}")
