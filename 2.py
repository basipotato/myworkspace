print("------10086查询功能------\n")
print("输入1,查询当前余额\n输入2，查询当前剩余流量\n输入3，查询当前剩余通话\n输入0，退出查询系统!\n")
while True:
    number = input()
    if number == "1":
        print("当前余额为：999")
    elif number == "2":
        print("当前剩余流量为：5G")
    elif number == "3":
        print("当前剩余通话为：189分钟")
    elif number == "0":
        print("退出查询系统！")
        break
