# # 元祖基本操作 - tuple -----> 元素可以重复，有序，不可修改
# # 定义
# t1 = (80, 95, 78, 50, 76, 80, 85, 20,)
#
# print(t1)
# print(type(t1))
#
# # 索引访问
# print(t1[0])
# print(t1[-1])
#
# # 切片
# print(t1[::1])
#
#
# #count() 统计元素的个数
# print(t1.count(80))
#
#
# #index() 获取元素的索引（第一个元素的位置）
# print(t1.index(80))
#
# #注意点：如果定义单元素的元组，单个元素后面要加上逗号，比如（100，）
# t2 = ()
# print(t2)
# t3 = (100,)
# print(type(t3))

# # 元组 tuple 组包与解包
# t1 = (5, 7, 9, 10, 2, 23, 12,)
# t2 = 5, 7, 9, 10, 2, 23, 12,
# print(t1)
# print(t2)
#
# # 组包操作
# a, b, c, d, e, f, g= t1
# print(a, b, c, d, e, f, g)
#
# first, second,*other,last = t1
# print(first, second)
# print(other)
# print(last)
#
# *other,last1,last2 = t1
# print(other)
# print(last1,last2)

# # 案例1：现在有两个变量，分别为：a = 100 , b = 20 现在要将这两个变量交换，然后输出到控制台
# a = 100
# b = 20
#a,b = b,a

# # 案例2:现有三个变量，分别为a = 100 , b = 200 ,c = 300 需将这三个变量等值交换，将a,b,c的值赋予c,a,b,并将其输出到控制台
# a = 100
# b = 200
# c = 300
# c,a,b = a,b,c
# print(a,b,c)


# 案例：根据提供的学生成绩单，完成一下需求
#     1.计算每个学生的总分，各科平均分，然后一并输出出来
#         2.统计各科成绩的最低分，最高分，平均分，并输出。
#         3.查找成绩优秀（平均分大于90）的学生并输出。
student = (
            ("s001","王林", 85, 92, 78),
            ("S001", "王林",  85, 92,  78),
            ("S002", "李慕婉", 92,  88,  95),
            ("S003", "十三", 78,  85, 82),
            ("S004",  "曾牛",  88,  79,  91),
            ( "S005",  "周轶",  95, 96,  89),
            ("S006", "王卓",  76,  82,  77),
            ("S007", "红蝶",  89,  91,  94),
            ("S008",  "徐立国",  75,  69,  82),
            ("S009",  "许木",  86,  89,  98),
            ("S010",  "道天",  66,  59, 72),
)

# 1.计算每个学生的总分，各科平均分，然后一并输出出来
# for s in student:
#     total = s[2] + s[3] + s[4]
#     avg = total / 3
#     print(f"{s[0]} \t{s[1]}\t {s[2]} \t{s[3]}\t {s[4]} \t{total}\t {avg:.1f} ")
# print()

# 方法2:
for id,name,chinese,math,english in student:
    total = chinese + math + english
    avg = total / 3
    print(f"{id} \t{name}\t {chinese} \t{math}\t {english} \t{total}\t {avg:.1f} ")
print()
  # 2.统计各科成绩的最低分，最高分，平均分，并输出
chinese_scores = [s[2]  for s in student]
math_scores = [s[3] for s in student]
english_scores = [s[4] for s in student]

print(f"语文成绩最低分：{min(chinese_scores)},最高分：{max(chinese_scores)},平均分：{sum(chinese_scores) / len(chinese_scores):.1f}")
print(f"数学成绩最低分：{min(math_scores)},最高分：{max(math_scores)},平均分：{sum(math_scores) / len(math_scores):.1f}")
print(f"英语成绩最低分：{min(english_scores)},最高分：{max(english_scores)},平均分：{sum(english_scores) / len(english_scores):.1f}")
print()

#         3.查找成绩优秀（平均分大于90）的学生并输出。
# print("优秀的同学有以下几位（平均分>90）")
# for s in student:
#     total = s[2] + s[3] + s[4]
#     avg = total / 3
#     if avg > 90:
#         print(f"{s[0]}\t{s[1]}\t\t{avg:.1f}")

# 方法2
print("优秀的同学有以下几位（平均分>90）")
for id,name,chinese,math,english in student:
    total = chinese + math + english
    avg = total / 3
    if avg > 90:
        print(f"{id}\t{name}\t\t{avg:.1f}")