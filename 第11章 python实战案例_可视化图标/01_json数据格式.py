# 学习目标
# 1.知道什么是json
# 2.掌握如何使用json进行数据转化

# 什么是json
# json本质上来说是一种带有特定格式的字符串
# json主要负责在各个编程语言中流通的数据格式,负责不同变成语言中的数据传递和交互

# json的格式:
# 1.字典
# 2.列表,但是列表中的元素都是字典


"""
演示json数据和python字典的相互转换
"""
# 导入json模块
import json

# 准备列表,列表内每个元素都是字典
data = [{"name": "张大山", "age": 11}, {"name": "王大锤", "age": 13}, {"name": "赵小虎", "age": 16}]
json_str = json.dumps(data, ensure_ascii=False)
print(type(json_str))
print(json_str)

# 准备字典,将字典转换为JSON
d = {"name": "周杰伦", "add": "台北"}
json_str = json.dumps(d, ensure_ascii=False)
print(type(json_str))
print(json_str)

# 将JSON字符串转换为Python数据类型
s = '[{"name": "张大山", "age": 11}, {"name": "王大锤", "age": 13}, {"name": "赵小虎", "age": 16}]'
l = json.loads(s)
print(type(l))
print(l)

# 将JSON字符串转换为Python数据类型
d = json.loads(s)
print(type(d))
print(d)
