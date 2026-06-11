# # for循环：遍历输入的字符串
#
msg = input("请输入需要遍历的字符串：")
for s in msg:
    print(f"元素：{s}")
else:
    print("遍历结束！")


# # 练习：计算1-100之间的奇数和。
# total = 0
# for i in range(0,101):
#     if i%2 != 0:
#         total += i
# else:
#     print(f"计算结束奇数总和为：{total}")

# # 练习：计算1-100之间的奇数和。（简化版）
# total = 0
# for i in range(1,101,2):
#         total += i
# else:
#     print(f"计算结束奇数总和为：{total}")

# # 练习:计算100-500所有3的倍数之和。
# total = 0
# for i in range(100,501):
#         if i%3 == 0:
#             total += i
# else:
#     print(f"计算结束奇数总和为：{total}")

# 案例：如下是一个长度为10，宽度为5的长方形
# **********
# **********
# **********
# **********
# **********
# print("*")自带换行效果，每一次执行都会输出新的一行中
# print("*", end = "  "):end表示的是每一次输出以什么结束;默认\n,表示换行。

# #1.接受键盘录入m , n
# # 长度
# m = int(input("请输入长度："))
# n = int(input("请输入宽度："))
# # 2.打印长方形
# for j in range(n):#控制行
#     for i in range(m):#控制列
#          print("*", end = "       ")
#     print()

# # 循环嵌套案例：打印99乘法表
# for i in range (1,10):
#     for j in range (1,i +1):
#         print(f"{j} x {i} = {i *j }",  end= "\t")
#     print()

# # 练习1:根据输入的直角边长，打印等腰直角三角形
# l = int(input("请输入直角边的边长："))
# for l in range(l+1):
#     for w in range(l):
#         print("*",end="    ")
#     print()

# #练习2:根据输入的数字，打印对应的数字金字塔
# for i in range(7):
#     for j in range(1,i+1):
#         print(f"{j}",end="    ")
#     print()

# # 练习3:打印国际象棋棋盘
# for i in range(8):      # 8行
#     for j in range(8):  # 8列
#         if (i + j) % 2 == 0:
#             print("X", end=" ")
#         else:
#             print("Y", end=" ")
#     print()  # 每行结束换行


#     案例：根据输入的用户名和密码执行登录操作，具体要求如下：
#     1.正确的用户名密码为 admin/666888、zhangsan/123456、taoge/888666
#     2.输入用户名密码进行登录，直到登录成功，程序结束运营；如果登录失败，则继续输入用户名和密码进行登录
#     3.输入用户名密码不能为空！
#     4.登录成功：输出“登录成功”，进入B站首页
#     5.登录失败：输出“用户名或密码错误，请重新输入！”

# break：只能出现在循环中，表示结束，跳出循环的含义（break跳出循环时，while后面的else中的代码不会执行）
# contlinue：智能出现在循环中，表示中断本次循环，直接进入下一次循环。


# while True :
#         username = input("请输入您的用户名：")
#         password = input("请输入您的密码：")
#         if username == "" or password == "":
#             print("用户名或密码不能为空！请重新输入。")
#             continue
#         elif username == "admin" and password =="666888" :
#             print("登录成功")
#             break
#         elif username == "zhangsan" and password =="123456" :
#             print("登录成功")
#             break
#         elif username == "taoge" and password == "888666" :
#             print("登录成功")
#             break
#         else :
#             print("输入错误，请重新输入")



# # 增加条件输入五次后将无法再次输入
# times = 0
# while True :
#         if times >= 5 :
#             print("您输入次数过多，无法继续输入。")
#             break
#         username = input("请输入您的用户名：")
#         password = input("请输入您的密码：")
#         if username == "" or password == "":
#             print("用户名或密码不能为空！请重新输入。")
#             times += 1
#             print(f"剩余尝试次数，{5 - times}")
#             continue
#         elif username == "admin" and password =="666888" :
#             print("登录成功")
#             break
#         elif username == "zhangsan" and password =="123456" :
#             print("登录成功")
#             break
#         elif username == "taoge" and password == "888666" :
#             print("登录成功")
#             break
#         else :
#             print("输入错误，请重新输入")
#             times += 1
#             print(f"剩余尝试次数，{5-times}")


# # 案例：猜数字游戏
# import random
# random_num = random.randint(1,100)#生成随机数
#
# time = 0
# while True :
#     if time == 5 :
#         print("您输入次数过多挑战失败")
#         print("太菜了！！！！")
#         break
#     num = int(input("请输入一个数字："))
#     if num > random_num :
#         print("您输入的数字太大了！")
#         time +=1
#     elif num < random_num :
#         print("你输入的数字太小了！")
#         time +=1
#     else:
#         print("太厉害了，这都被你猜到了！！！！")
#         break
# print("答案是：",random_num)


# # 练习1:将1-100之间所有的5的倍数的数字累加起来。
# num = 0
# for i in range(101):
#     if i % 5 == 0:
#         num += i
# print(f"计算结束5的倍数和为：{num}")


# # 练习2:统计字符串"akiwksjakdiklowiqaamnvbamvaxnsjdsjkaaxkjd"字符串中有多少个a和k。
# num = 0
# nub  = 0
# for i in "akiwksjakdiklowiqaamnvbamvaxnsjdsjkaaxkjd":
#     if i == "a":
#         nub += 1
#     elif i == "k":
#         num += 1
# print(f"a一共有{nub}个")
# print(f"k一共有{num}个")