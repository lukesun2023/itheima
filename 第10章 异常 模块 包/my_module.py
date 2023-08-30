__all__ = ['testA'] # 控制from my_module import *中,*包括的内容


def testA(a, b):
    print(a + b)


def testB(a, b):
    print(a - b)


if __name__ == "__main__":
    testA(1, 2)
# end main
