# 一个函数中只会执行一个return,当函数执行到return语句时,函数就会终止
# 函数返回多个返回值的语法:
# return 1, 2

def test_return():
    return 1, "hello", True


x, y, z = test_return()
print(x)
print(y)
print(z)

# NOTE 返回值的数量不限,注意接收返回值的变量的数量和位置与return语句一一对应
# 返回值的数据类型不受限制
