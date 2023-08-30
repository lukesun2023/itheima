# 字符串的大小比较基于对应的ASCII码表值
# 字符串的大小比较是按位比较,一位一位的进行,只要有一位大,那么整体就大

# abc 比较 abd
print(f"abd大于abc,结果:{'abd' > 'abc'}")

# a 比较 ab
print(f"ab大于a,结果:{'ab' > 'a'}")

# a 比较 A
print(f"a大于A,结果:{'a' > 'A'}")

# key1 比较 key2
print(f"key2大于key1,结果:{'key2' > 'key1'}")
