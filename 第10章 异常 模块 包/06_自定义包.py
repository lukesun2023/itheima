# python包的作用就是管理模块,从物理上来说,python包就是文件夹.
# python包主要包括两类文件1.模块 2.__init__.py

# 创建一个包
# 导入自定的保重的模块,并使用
# import my_package.my_module1
# import my_package.my_module2
#
# my_package.my_module1.info_print1()
# my_package.my_module2.info_print2()

from my_package import my_module1
from my_package import my_module2
my_module1.info_print1()
my_module2.info_print2()

