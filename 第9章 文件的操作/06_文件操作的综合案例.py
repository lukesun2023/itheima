# 打开文件
f = open(r"第9章 文件的操作\bill.txt", "r", encoding="UTF-8")
g = open(r"第9章 文件的操作\bill_backup.txt", "w", encoding="UTF-8")

# 使用readlines读取文件,将列表赋予lines
lines = f.readlines()

# 使用for遍历包括文件全部内容的lines列表,获得每行的内容
for line in lines:
    # 使用标志 flag
    flag = False
    # 对字符串的切片进行处理,判断每行的关键字是正式还是测试
    line_backup = line[:]
    line_backup = line_backup.strip()
    line_backup = line_backup.split(",")

    for word in line_backup:
        if word == "正式":
            flag = True
            g.write(line)

# 关闭文件
f.close()
g.close()
