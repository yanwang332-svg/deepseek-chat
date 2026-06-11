# # if条件判断，如果分数超过680，我就去清华读书
# score = 690
# if score >= 680:
#     print("欢迎来到清华读书")
#     print("也恭喜你即将踏入精彩的大学生活")
#
# print("______________________________")

# 案例：需求：结合前面学习的输入输出及if条件判断的知识，完成B站登录功能的实现（正确的账号和密码为18888888888/666888）
# 接收正确的账号密码
# ok_account  = "1888888888"
# ok_password = "666888"
# # 1.接受用户输入账号和密码
# account= input("请输入您的B站账号：")
# password = input("请输入正确的B站密码")
# # 2.判断账号和密码是否全部正确，如果都正确，则登录成功，进入B站首页
# if account == ok_account and password == ok_password:
#     print("登录成功")
#     print("进入B站首页")
# # 3.判断账号和密码是否有错误的，如果有错误信息，则登录失败，提示错误信息
# if account != ok_account or password != ok_password:
#     print("登录失败")
#     print("请输入正确的账号和密码")

#
# ok_account  = "1888888888"
# ok_password = "666888"
# # 1.接受用户输入账号和密码
# account= input("请输入您的B站账号：")
# password = input("请输入正确的B站密码")
# # 2.判断账号和密码是否全部正确，如果都正确，则登录成功，进入B站首页
# if account == ok_account and password == ok_password:
#     print("登录成功")
#     print("进入B站首页")
# # 3.判断账号和密码是否有错误的，如果有错误信息，则登录失败，提示错误信息
# else:
#     print("登录失败")
#     print("请输入正确的账号和密码")


#     # 案例：根据用户输入的年份，判断这一年是闰年还是平年
# year = int( input("请输入年份："))
# if (year % 100 !=0 and year%4  == 0) or (year % 400 ==0 ):
#     print(f"{year}是闰年")
# else:
#     print(f"{year}是平年")

# # 练习题1.根据用户输入的数字判断是奇数还是偶数
# nub = int(input("请输入需要判断的数字"))
# if nub%2 == 0 :
#     print(f"{nub}是偶数")
# else:
#     print(f"{nub}是奇数")

# # 练习题2.根据用户输入的年纪，判断该用户是否成年
# age = int(input("请输入你的年龄"))
# if age >= 18:
#     print("您已成年")
# else :
#     print("您未成年")

# # 练习题3.根据用户输入的数字判断该数字是正数还是负数（不考虑0）
# nub =int( input("请输入数字："))
# if nub > 0 and nub !=0:
#     print(f"{nub}是正数")
# else:
#     print(f"{nub}是负数")

# 练习题4.根据用户输入的考试分数，判断是否及格

# score = int(input("请查询您的科目成绩："))
# # a = int(84) #语文
# # b = int(25)# 数学
# # c = int(10)# 英语
# if score >=60:
#     print(f"{score}及格")
# else :
#     print(f"{score}不及格")


# # 练习题3.根据用户输入的数字判断该数字是正数还是负数（考虑0）
# nub =float( input("请输入数字："))
# if nub > 0 :
#     print(f"{nub}是正数")
# elif nub < 0 :
#     print(f"{nub}是负数")
# else :
#     print(f"{nub}是0")

# # 案例：请输入用户名、密码进行登录系统
# #     用户名、密码为：admin/666888 或 root/547527 或 zhangsan/123456 则输出登录成功
# #     否则就提示用户名或者密码错误
# account1= "admin"
# password1 = "666888"
# account2 = "root"
# password2 = "547527"
# account3 = "zhangsan"
# password3 = "123456"
# account = input("请输入账号：")
# password  = input("请输入密码：")
# if account == account1 and password == password1:
#     print("欢迎登陆")
# elif account == account2 and password == password2:
#     print("欢迎登陆")
# elif account == account3 and password == password3:
#     print("欢迎登陆")
# else :
#     print("登录失败请检查账户密码")

# # 练习1:根据输入的考试成绩，判断成绩等级。
#     #     大于等于85分为优秀
#     #     60-85分为及格
#     #     否则就是不及格
# score = int(input("请输入您的考试成绩："))
# if score > 85 :
#     print(f"您的成绩：{score}为优秀")
# elif 60 < score < 85:
#     print(f"您的成绩：{score}为及格")
# else:
#     print(f"您的成绩：{score}为不及格")

# # 练习2:根据输入购物车的商品总额，以及如下的折扣规则，计算实际应付的金额。
# #     金额 >= 500：8折
# #     300 <= 金额 < 500 : 9折
# #     100 <= 金额 < 300 :9.5 折
# #     金额 < 100 :无折扣
# amount = float(input("请输入您的购物金额"))
# if amount >= 500:
#         print(f"您的消费金额为(8折)：{amount*0.8}")
# elif 300 <= amount <500 :
#         print(f"您的消费金额为(9折)：{amount*0.9}")
# elif 100 <= amount < 300 :
#         print(f"您的消费金额为(95折)：{amount*0.95}")
# else:
#         print(f"你的金额为：{amount}")
"""
if else 结课练习
    北京市居民用电电费计算：根据输入的用电度数，计算电费
        北京市居民电费采用阶梯电价计价方式，所谓阶梯电价是指按照用户消费的电量分段定价
        用电价格随用电量增加呈现阶梯状逐级递增的一种电价定价机制
        阶梯电价规则：
            第一档：2880度以下，电费单价0.4883元/度
            第二档：2880-4800度，电费单价0.5383元/度
            第三档：4800度以上，电费单价0.7883元/度
"""
from turtledemo import two_canvases

fee = float(input('请输入您的用电度数: '))

if fee <= 2880:
    # 第一档
    total = fee * 0.4883
    print(f'您的用电量为{fee}度')
    print(f'电费为: {total:.2f}元')

elif 2880 < fee <= 4800:
    # 第一档 + 第二档
    first = 2880 * 0.4883
    second = (fee - 2880) * 0.5383
    total = first + second
    print(f'您的用电量为{fee}度')
    print(f'第一档电费: {first:.2f}元')
    print(f'第二档电费: {second:.2f}元')
    print(f'总电费: {total:.2f}元')

else:
    # 第一档 + 第二档 + 第三档 (fee > 4800)
    first = 2880 * 0.4883
    second = (4800 - 2880) * 0.5383
    third = (fee - 4800) * 0.7883
    total = first + second + third
    print(f'您的用电量为{fee}度')
    print(f'第一档电费: {first:.2f}元')
    print(f'第二档电费: {second:.2f}元')
    print(f'第三档电费: {third:.2f}元')
    print(f'总电费: {total:.2f}元')