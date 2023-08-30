# 普通字符串拼接的缺点:
# 1.变量过多,拼接起来麻烦;
# 2.字符串无法和数字或其他类型完成拼接.
class_num = 57
avg_salary = 16781
message = "Python大数据学科,北京%s期,毕业平均工资:%s" % (class_num, avg_salary)
print(message)
message = f"Python大数据学科,北京{class_num}期,毕业平均工资:{avg_salary}"
print(message)

name = '黑马程序员'
message = "学IT来: %s" % name
print(message)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# 最常用的三种占位形式:
# %s 将内容转换成字符串,放入占位位置
# %d 将内容转换成整数,放入占位位置
# %f 将内容转换成浮点数,放入占位位置
name = "传智播客"
set_up_year = 2006
stock_price = 19.99
message = "我是:%s, 我成立于%d,我今天的股票价格是:%f" % (name, set_up_year, stock_price)
print(message)
