my_list = ['黑马程序员', '传智播客', '传智播客', 'itheima',
           'itcast', 'itheima', 'itcast', 'best']
# NOTE 定义空集合的方法比较特别，必须用set()
my_set = set()

for element in my_list:
    my_set.add(element)

print(f"将列表my_list中的元素转移到集合my_set中，my_set为：{my_set}")
