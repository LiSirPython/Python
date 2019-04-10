# -*- coding: UTF-8 -*-
#random模块的randit方法生成随机数
import random
menu = ["减肥", "宫保鸡丁", "酸辣土豆丝", "米线", "炒饭", "面食", "鱼香肉丝", "涮锅", "煎饼", "烤冷面", "黄记煌", "海底捞"]
while True:
    print("今天的菜品：", menu)
    lunch=input("请问您想吃什么？如果您不知道吃什么，可以让系统推荐\n")
    if lunch is None:
        print("您没有输入任何信息，请重新下单")
        continue
    elif lunch in menu:
        print("下单成功！")
        print("您的点餐为：",lunch)
        break
    elif lunch == "推荐":
        num = random.randint(0, 11)
        print("系统为您推荐的是：",menu[num])
    else:
        print("没有您想要的菜品，请重新下单")
        continue
