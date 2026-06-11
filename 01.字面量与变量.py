# from enum import nonmember  # 字面量写法
# print(1010)#整数（int）
# print(3.14)#浮点数/小数（float）
# print(True)#布尔（bool）
# print(False)#布尔（bool）
# print("hello python")#字符串（str）
# print(None)#空值（NoneType）
#
# # 布尔类型本质也是整数类型（True -1;false-0）
# print(True-1)
# print(False-1)
from collections.abc import async_generator
from email.mime import base
from os import name

# 哈哈哈 = 110
# print(哈哈哈)
# sso = "kkluve"
# print(sso)
# sso = "kkluve"
# print(sso)

# base,lucx,fpx,lcc = 27.9,50,90,2
# print("播放量第一个月增加：",base+lucx+fpx*lcc)


# a,b,c = 100,200,300
# d = a
# a = b
# b = c
# c = d
# print(c,a,b)

# # 字符串拼接
# misg = "这里的山路十八弯"
# misg2 = "这里的水路九连环"
# print("gai:"+misg+" , "+misg2)

name = "王琰"
age = 31
pro = "设计师"
hobby = "python,java"
# print(name)
# print(age)
# print(pro)
# print(hobby)
# print("大家好，我是" + name + ",今年" + str(age) + "岁," + "我的职业是" + pro + "," + ''"爱好"+ hobby + ".")


# print("大家好，我是%s,今年%s岁,我的职业是%s,爱好%s."%(name,age,pro,hobby))


print(f"大家好，我是{name},今年{age}岁,我的职业是{pro},爱好{hobby}")