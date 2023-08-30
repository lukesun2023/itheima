# 文件追加模式

# 打开不存在的文件
f = open(r"d:\python\itheima\test1.txt", "a", encoding="UTF-8")
# write写入
f.write("黑马程序员")
# flush刷新
f.flush()
# 关闭文件
f.close()
# NOTE a模式打开不存在的文件会新创建一个文件并且写入内容

# 再次打开刚创建的文件(打开已经存在的文件)
f = open(r"d:\python\itheima\test1.text", "a", encoding="UTF-8")
# 对文件进行写入操作
f.write("\n学python最佳选择")
# flush
f.flush()
# close
f.close()
