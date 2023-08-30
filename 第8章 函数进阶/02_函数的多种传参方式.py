# 函数的传参方式:
# 位置参数:
# 传递参数时根据函数定义的参数位置来传递参数(实参和形参根据排列顺序一一对应)
# 关键字传递参数:
# 传参时通过"键=值"的形式传递参数
# 关键字传递参数可以不考虑位置顺序,只要关键字对应准确,就能保证实参和形参的一一对应
# 关键字传参和位置参数混用的时候,要把关键字传参的参数放在后面,将位置参数按照传参的要求放在前面


# 实例演示:
def user_info(name, age, gender):
    print(f"姓名是:{name}, 年龄是:{age}, 性别是:{gender}")


# 位置参数
user_info(20, '小明', '男')


# 关键字传参
user_info(name='小明', age=18, gender='男')

# 关键字传参和位置参数
user_info('甜甜', gender='女', age=19)


# 缺省参数:
# 在定义函数的时候给参数设定默认值,如果调用函数的时候重新给该参数赋值则使用新赋的值,否则使用默认值
# NOTE 使用带有默认值的缺省参数必须放在参数队列的最后面,位置参数必须放在参数队列的最前面
def user_info(name, age, gender='男'):
    print(f"姓名是:{name}, 年龄是:{age}, 性别是:{gender}")


# 不给gender另外传递实参,使用默认值'男'
user_info('小天', 13)


# 不定长参数:
# 1.位置传递的不定长参数
# 使用的参数名为*args,默认标记为一个元组类型,传递的元素都会传递到元组内部
# 不定长参数的args不是规定,而是用约定俗成,但是*不能省略
def user_info(*args):
    print(args)


# ('TOM')
user_info('TOM')
user_info('TOM', 'Jaro')


# 2.关键字传递的不定长参数
# 关键字传递的不定长参数,所有的'键=值'都会被kwargs接收,并组成字典
def user_info(**kwargs):
    print(kwargs)


# {'name': 'TOM', 'age': 18, 'id': 110}
user_info(name='TOM', age=18, id=110)
