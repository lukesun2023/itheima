# 打开原始文件
fr = open(r"第9章 文件的操作\bill.txt", "r", encoding="UTF-8")
# 打开文件得到文件对象,准备写入
fw = open(r"第9章 文件的操作\bill.txt.back", "w", encoding="UTF-8")
for line in fr:
    # 清除掉字符串中开头和结尾的空格和换行符
    line = line.strip()

    # 通过','将字符串分割成新的列表
    if line.split(",")[4] == "测试":
        continue

    print(type(line))
    
    # 将内容写入
    fw.write(line)
    # 由于前面对内容进行strip()的操作,要再次添加上换行符
    fw.write("\n")

# 关闭文件
fr.close()
fw.close()
