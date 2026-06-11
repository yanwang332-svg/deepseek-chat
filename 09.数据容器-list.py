# # 列表操作
# # 定义列表-list
# s = [55 , 67 , 108 , True, "hello", "你好"]
# print(type(s))
#
# # 访问列表元素
# # 获取
# print(s[-1])#反向索引，从-1开始
# print(s[5])#正向索引从0开始
#
# #修改
# s[3] = False
# print(s)
#
# #注意：如果指定的索引，超出范围，将会报错
#
# #   删除
# del s[-2]
# print(s)
#
# # 遍历
# for i in s :
#     print(i)
from hashlib import new

# s = [12 , 34 , 76 , 88 , 9 ,33 , 88 , 99 , 34 , 678 , 999 , 256 ]
#
# s.append(999)#在列表尾部增加元素
# print(s)
#
# s.insert(3,88)#在指定索引前插入该元素
# print(s)
#
# s.remove(88)#移除列表中第一个匹配到的值
# print(s)
#
# s.pop()#删除列表行中指定索引位置的元素（如果未指定索引，默认删除最后一个）
# print(s)
#
# s.sort()#对列表进行排序（列表元素的数据类型一致，才可以进行排序）
# print(s)
#
# s.reverse()#反转列表元素
# print(s)

# 案例1：根据用户输入的10个数字，储存到一个列表中，并将列表中数字排序，输出其中的最小值、最大值和平均值。

# num_list = []
#
# for i in range(10):
#     num = int(input("请输入一个有效数字："))
#     num_list.append(num)
# print("数字列表：" , num_list)
#
# num_list.sort()
# print("排序后的数字列表：" , num_list)
# print("最大值：" , num_list[-1])
# print("最小值：" , num_list[0])
# print("平均值：" , sum(num_list)/len(num_list))#sum() 求和；len() 获取元素个数（列表的长度）


# 案例2：合并两个列表中的元素，并对合并的结果进行去重处理（取出列表中的重复元素）
num_list1 = [19 , 23 , 54 , 64 , 875 , 20 , 209 , 232 , 123 , 54]
num_list2 = [55 , 80 , 72 , 35 , 60 , 123 , 54 , 29 , 91 ]

# for num in num_list2:
#     num_list1.append(num)
# print(num_list1)
# num_list1.sort()
# print(num_list1)
# new_list = []
# for num in num_list1:
#     if num not  in new_list:#判断元素是否存在于列表中，如果存在，则返回，不存在则继续
#         new_list.append(num)
# print(new_list)

# # 简化版1
# #解包：*  将列表一类容器解开成一个一个独立的元素
# # 组包：将多个值合并到一个容器
# num_list = [*num_list1, *num_list2]
# print(num_list)
# num_list1.sort()
# print(num_list1)
# new_list = []
# for num in num_list1:
#     if num not  in new_list:#判断元素是否存在于列表中，如果存在，则返回，不存在则继续
#         new_list.append(num)
# print(new_list)

# # 简化版2
# num_list  = num_list1 + num_list2
# print(num_list)
# num_list1.sort()
# print(num_list1)
# new_list = []
# for num in num_list1:
#     if num not  in new_list:#判断元素是否存在于列表中，如果存在，则返回，不存在则继续
#         new_list.append(num)
# print(new_list)

# # 案例：生成1-20的平方列表（传统方式）
# num = []
# for i  in range (1,21) :
#     num .append(i**2)
# print(num)


# # 案例：生成1-20的平方列表（方式二列表推导式 ----按照一定规则快速生成一个列表的方法----语法格式：[要插入的值 for i in 序列/列表]）
# num_list = [i**2 for i in range(1,21)]
# print(num_list)


# # 案例2:从一个数字列中提取所有偶数，并计算其平方，组成一个新的列表。
# #[要插入的值 for i in 序列/列表 if 条件判断]
# num_list = [12 , 32 , 45 , 77 , 88 , 92 , 33 , 57 , 97 ,98]
# new_list= [i**2 for i in num_list if i %2 == 0]
# print(new_list)
#
# # 练习1；将如下多个列表和为一个列表，并去重重复元素，排序后输出到控制台。
# list1 =["M" , "A" , "C" , "E" , "F" , "G" , "H" , "L" , "N" , "I" , "J" , "K" , "O" , ]
# list2 = ["X" , "Z" , "T" , "Y" , "D" , "E" , "F" , "G"]
# list3 = ["W" , "A" , "S" , "D"]
#
# num = [*list1, *list2, *list3]
# print(num)
# nwe_list = []
# for i in num:
#     if i not in nwe_list :
#         nwe_list.append(i)
#         nwe_list.sort()
# print(nwe_list)

# # 练习2：将如下列表中能被3或5整除的元素提出来，并获得这些数字相应的平方，组成一个新的列表
# listl = [1, 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20 , 21 , 22 , 23 , 24 , 25 , 26 , 27 , 28 , 29 , 30]
# num_list = [i**2 for i in listl if i%3 == 0 or  i%5 == 0]
# print(num_list)

# # 练习3：将如下列表中的整数提取出来，封装为一个新的列表。
# list1 = [11 , 2 , 31 , 4 , -5 , 15 , 17 , 28 ,49 , 10 , -11 ,16 , 54 , -14 ,36 ,-16 , 87 , -39]
# new_list = [i  for i in list1 if i >= 0]
# new_list.sort()
# print(new_list)

