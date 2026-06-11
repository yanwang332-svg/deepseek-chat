# from ast import literal_eval
#
# print("10+4=",10+4)
# print("10-4=",10-4)
# print("10*4=",10*4)
# print("10/4=",10/4)
# print("10//4=",10//4)
# print("10**4=",10**4)
# print("65471%339=",65471%339)
import decimal
from decimal import Decimal

# # 案例：输入x和y，计算x+y和x-y的结果并输出
# x = Decimal(input("请输入x的值："))
# y = Decimal(input("请输入y的值："))
# print("x+y=",x+y)
# print("x-y=",x-y)
#
# # 训练1:计算输入的三个整数的平均数
# x = int( input("数值1:"))
# y = int(input("数值2:"))
# z = int(input("数值3:"))
# print("平均值为",(x+y+z)/3)

# # 训练2:要求输入圆的半径，计算圆的周长（周长：2π   面积：r™）
# # π = 3.14159
# from math import pi   # 从库中调用π的公式
#
# r = int(input("半径："))
# print("圆的周长：" , 2*pi*r)
# print(f"圆的面积：{pi*r**2:.2f}")

# 训练3:身体质量指数BMI的计算（BMI = 体重（kg）/ 身高（m）™）
# 1.输入体重（单位kg）
# 2.输入身高（单位m）
# 3.计算身体质量指数BMI并输出
# kg =float(input("体重数值："));
# m = float(input("身高数值："))
# print(f"BMI={kg/m**2:.2f}")

# num = 85
# num += 10
# print("num +=10 ",num)
# num -= 10
# print("num -=10 ",num)
# num *= 10
# print("num *=10 ",num)
# num /= 10
# print("num /= 10 ",num)
# num %= 3
# print("num %=10 ",num)
# num **= 10
# print("num **=10 ",num)
# num //= 10
# print("num //=10 ",num)

# # 比较运算符
# print("100 == 100 吗:",100 == 100)
# print("你好 == 您好吗：","你好" == "您好")
# print("100 != 100 吗：",100 != 100)
# print("100 < 100 吗：",100 < 100)
# print("100 <= 100 吗：",100 <= 100)
# print("100 > 100 吗：",100 > 100)
# print("100 >= 100 吗：",100 >= 100)
#
# # 逻辑运算符
# # 案例1，键盘输入一个整数，判断这个数是否在10--20之间
# n = int(input("请输入一个整数"))
# print(f"{n}在10-20之间：", n >= 10 and n <= 20)
# # print(f"{n}在10-20之间：", 10 <= n <= 20)
# 案例2，键盘输入一个整数，判断这个数是否不在10--20之间
# n = int(input("请输入一个整数"))
# print(f"{n}不在10-20之间：", n < 10 or  n > 20)