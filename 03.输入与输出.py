# # 获取键盘上的输入数据--->>>input
# name = input("请输入你的姓名：")
# age = input("请输入你的年龄：")
# print(f"我的姓名是{name},我的年龄是{age}.")
from calendar import firstweekday

# 银行卡ATM取款项目训练
# 总金额
total = 10000
# 1.输入密码
passyword = input("请输入您的银行密码：")
print(f"密码正确，{passyword}")
# 2.输入取款金额
num = input("请输入取款金额：")
# 3.计算金额并输出
print(f"您的余额还剩：{total - int(num)}")
# balance = {total-int(num)}
# total = balance

# 练习题：根据客户输入的两个数字，计算两个数字之和，并将其输出到控制台
firstinput = input("第一次输入；")
secondinput = input("第二次输入：")
print(f"最终结果：{int(firstinput)+int(secondinput)}")