# 可以使用辅助符号"m.n"来控制数据的宽度和精度
# m,控制宽度,要求是数字(很少使用),设置的宽度小于数字自身的时候,不生效
# n,控制小数点精度,要求是数字,会进行小数的四舍五入
# 例如在格式的过程中:
# %5d:表示整数的宽度控制在5位,如数字11,被设置为5d,就会变成:[空格][空格][空格]11,用三个空格补足宽度
# %5.2f:表示将宽度控制为5,将小数点精度设置为2
# %7.2f:对11.345设置,输出的结果为:[空格][空格]11.35,两个空格是为了补足宽度为7的要求
# %2f:表示不限制宽度,只现值小数的精度

num1 = 11
num2 = 11.345
print("数字11宽度现值5,结果是:%5d" % num1)
print("数字11宽度现值1,结果是:%1d" % num1)
print("数字11.345宽度现值7,小数精度2,结果为%7.2f" % num2)
print("数字11.345宽度不限制,小数精度2,结果是:%.2f" % num2)
