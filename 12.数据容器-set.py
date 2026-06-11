# # # 集合 set
# # # 定义
# # s1 ={5, 3, 2, 0, 9, 12, 43, 64, 22, 5, 0}
# # print(s1)
# # print(type(s1))
# #
# # # 定义空集合
# # s2 = set()
# # print(s2)
# # print(type(s2))
# import site
# from operator import add
#
# from pygame.event import clear
#
# # 常见方法
# # add():添加元素到集合
# s1 = {100, 200, 300, 400, 500, 600, 700, 800}
# print(s1)
# s1.add(1200)
# print(s1)
#
# # remove()：移除集合中指定元素（指定元素不存在将报错）
# s1.remove(1200)
# print(s1)
#
# # pop();随即删除集合中的元素并返回
# e = s1.pop()
# print(e)
# print(s1)
#
# # clear():请空集合
# s1.clear()
# print(s1)


# s2 = {"A","B"," D","K", "L","I","P", "Y", "H"}
# s3 = {"A", "K", "I", "L", "Q", "N",}
# difference() :求两个集合的差集（存在于第一个集合不存在于第二个集合
# print(s2.difference(s3))
# print(s3.difference(s2))

#union(): 求两个集合的并集
# print(s2.union(s3))

#intersection() :求两个集合的交集
# print(s2.intersection(s3))

# 案例：根据提供的班级学生选课情况，完成如下需求：
# 选修足球学生名单
football_set = {"王林", "曾牛", "徐立国", "遁天", "天运子", "韩立", "厉飞雨", "乌丑", "紫灵"}

# 选修篮球学生名单
basketball_set = {"张铁", "墨居仁", "王林", "姜老道", "曾牛", "王蝉", "韩立", "天运子", "李化元", "厉飞雨", "云露"}

# 选修法语学生名单
french_set = {"许木", "王卓", "十三", "虎鸣", "姜老道", "天运子", "红蝶", "厉飞雨", "韩立", "曾牛"}

# 选修艺术学生名单
art_set = {"遁天", "天运子", "韩立", "虎鸣", "姜老道", "紫灵"}

# 1.找出同时选秀法语和艺术的学生
fa_set = french_set.intersection(art_set)
print(f"同时选修了 法语 和 艺术的 学生：{fa_set}")
# 方法二：&---->交集
fa_set1 = french_set&art_set
print(f"同时选修了 法语 和 艺术的 学生：{fa_set1}")
#2.找出同时选修4门课的学生
all_set = football_set & basketball_set & french_set & art_set
print(f"同时选修了四门课程的学生: {all_set}")

#3.找出选休足球但是没选修篮球的学生
fb_set = football_set .difference(basketball_set)
print(f"选修足球但是没选修篮球的学生：: {fb_set}")

#方法二：-   ------> 差集
fb_set1 = football_set - basketball_set
print(f"选修足球但是没选修篮球的学生：: {fb_set1}")

#方法三：集合推导式 ----> 快速构建集合 ，语法：{要往集合中添加的元素 for in set if 条件}
fb_set3 = {s for s in football_set if s not in basketball_set}
print(f"选修足球但是没选修篮球的学生：: {fb_set3}")
# 4.统计每一个学生选修的课程数量
#4.1 获取学生名单 -- 并集 （  ｜  ）
all_set= football_set | basketball_set | french_set | art_set
#4.2 获取每一个学生选择的课程数量
all_list = [*football_set,*basketball_set,*french_set,*art_set]
for s in all_set:
    print(f"{s}选修了{all_list.count(s)}课程")