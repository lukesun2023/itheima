import random
num = random.randint(1, 10)

num_guess = int(input("你猜猜这个随机数是多少?"))

if num == num_guess:
    print("恭喜你,答对了!")
else:
    if num_guess > num:
        print("不好意思,你猜的数大了!")
    else:
        print("不好意思,你猜的数小了!")

    num_guess = int(input("请再猜猜这个随机数是多少?"))

    if num_guess == num:
        print("恭喜你,答对了!")
    else:
        if num_guess > num:
            print('不好意思,你猜的数大了!')
        else:
            print("不好意思,你猜的数小了!")

        num_guess = int(input("请最后再猜一次这个随机数是多少?"))

        if num_guess == num:
            print("恭喜你,终于猜对了!")
        else:
            if num_guess > num:
                print("很遗憾,你猜的数大了!")
            else:
                print("很遗憾,你猜的数小了!")

            print("这个数是%d" % num)
