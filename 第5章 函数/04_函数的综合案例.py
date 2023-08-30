def main_menu():
    """
    输入用户名后的主要交互界面
    :return:用户选择操作的序号(1~4)
    """
    print("---------------------主菜单---------------------")
    print(f"{name}，您好，欢迎来到黑马银行ATM，请选择操作：")
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    selection = int(input("请输入您的选择:"))
    return selection


def check_cash_balance(name, money):
    """
    显示客户存款余额
    :param name:客户姓名
    :param money:客户现金余额
    """
    print("---------------------查询余额---------------------")
    print(f"{name}，您好，您的余额剩余:{money}")


def deposit(name, cash):
    """
    要求客户输入存款金额，并显示账户余额
    :param cash:余存款额
    :return:存款后的现金余额
    """
    deposit_cash = int(input("请输入您的存款金额："))
    cash += deposit_cash
    print("---------------------存款---------------------")
    print(f"{name},您好，您存款{deposit_cash}元成功\n您的存款余额为：{cash}")
    return cash


def withdrawal(name, cash):
    """
    要求客户输入取款金额，并显示账户余额
    :param cash:存款余额
    :return:取款后的现金余额
    """
    withdrawal_amount = int(input("请输入您的取款金额："))
    cash -= withdrawal_amount
    print("---------------------取款---------------------")
    print(f"{name},您好，您取款{withdrawal_amount}元成功\n您的存款余额为：{cash}")
    return cash


# 初始化两个全局变量
money = 5000000
name = input("请输入您的姓名：")
flag = True

# 菜单进行循环显示
while flag:
    select_num = main_menu()
    if select_num == 1:
        check_cash_balance(name, money)
        continue
    elif select_num == 2:
        money = deposit(name, money)
        continue
    elif select_num == 3:
        money = withdrawal(name, money)
        continue
    elif select_num == 4:
        print("您选择了退出系统！")
        break
    else:
        print("输入错误，系统终止！")
        break
