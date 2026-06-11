# 字典
# 定义字典
"""
dict1 = {"王林": 670, "李慕婉" : 608 , "徐立国" : 580 , "韩立" : 688}

print(dict1)
print(type(dict1))

#key必须是不可变类型（str,int,float,tuple）,不能是 list，set，dict
dict2 = {0:670, 1:608, (1,2):580, ("A","B"):688}
print(dict2)

#访问
print(dict1["王林"])#获取
dict1["王林"] = 690 #修改
print(dict1)
"""
from platform import mac_ver

# from itertools import count
# from os import times_result

# dict1 = {"王林": 670, "李慕婉" : 608 , "徐立国" : 580 , "韩立" : 688}
# print(dict1)
#
# # 添加 -- key不存在就是添加
# dict1["涛哥"] = 550
# print(dict1)
#
# #修改 -- key存在就是修改
# dict1["涛哥"] = 610
# print(dict1)
#
# #查询
# print(dict1["涛哥"])#根据key获取value
# print(dict1.get("涛哥"))#根据key获取value
#
#
# print(dict1.keys())#获取所有key
# print(dict1.values())#获取所有value
# print(dict1.items())#获取所有的键值对 key：value
#
#
# #删除
# score = dict1.pop("徐立国")
# print(score)
# print(dict1)
#
# del dict1["涛哥"]
# print(dict1)
#
# #遍历
# for k in dict1.keys():
#     print(f"{k}:{dict1[k]}")
#
# for i in dict1.items():
#     print(f"{i[0]};{i[1]}")
#
# for k, v in dict1.items():
#     print(f"{k}:{v}")

"""
案例：开发一个购物车管理系统，实现商品信息的添加、修改、查询功能。系统使用字典结构储存商品数据，
             通过控制台菜单与用户交互。剧透功能如下：
            1.添加购物车：用户根据录入商品名称、以及该商品价格、数量、保存该商品到购物车。
            2.修改购物车：用户输入要修改的购物车商品名称，然后再提示输入该商品价格、数量
                输入完成后修改该商品信息。
            3.删除购物差：要求用户输入要删除的购物车名称，根据名称删除购物车中商品。
            4.查询购物车：将购物车中的商品信息展示出来，格式为：“商品名称，xxxx，商品价格：
                xxxxx，商品数量”。
            5.退出购物车。
            结构：shopping_cart = {"商品"：{"价格：xxxx,"数量"：xxxx"},"商品：{"价格：xxxx,"数量"：xxxx"}，····}
"""
# # 添加购物车
# sp_cart = {}
# print("欢迎使用购物车系统")
# menu = """
# ###############购物车系统###############
# #                                      1.添加购物车                                   #
# #                                      2.修改购物车                                  #
# #                                      3.删除购物车                                  #
# #                                      4.查询购物车                                  #
# #                                      5.退出购物车                                  #
# #######################################
# """
#
# while True:
#     print(menu)
#     choice = input("请选择要执行的操作（1-5）")
#
#     match choice:
#         case "1":  # 添加购物和
#             goods_name = input("请输入商品名称:")
#             goods_price = float(input("请输入商品价格："))
#             goods_num = int(input("请输入商品数量："))
#             # 如果商品存在，则不执行添加，返回提示信息
#             if goods_name in sp_cart:
#                 print("商品已存在，请勿重复添加")
#             else:
#                 sp_cart[goods_name] = {"价格": goods_price, "数量": goods_num}
#                 print("商品添加完成")
#         case "2":  # 修改购物车
#             goods_name = input("请输入要修改的商品名称:")
#             if goods_name not in sp_cart:
#                 print("暂未找到该商品，请重新输入")
#                 continue
#             goods_price = float(input("请输入商品最新的价格："))
#             goods_num = int(input("请输入商品最新的数量："))
#             sp_cart[goods_name] = {"价格": goods_price, "数量": goods_num}
#             print("商品修改完成")
#
#         case "3":  # 删除购物车
#             goods_name = input("请输入要删除的商品名称")
#             # 如果商品不错在，则提示错误信息，重新选择
#             if goods_name not in sp_cart:
#                 print("该商品不存在，请重新选择")
#             else:
#                 del sp_cart[goods_name]
#                 print("商品删除完毕")
#
#         case "4":  # 查询购物车
#             for goods_name in sp_cart.keys():
#                 goods_info = sp_cart[goods_name]
#                 print(f"商品名称：{goods_name},商品价格：{goods_info["价格"]},商品数量：{goods_info["数量"]}")
#         case "5":  # 退出
#            print("bye bye")
#            break
#         case _:  # 匹配其他语法直接用下划线
#             print("非法操作，暂不支持")



"""
练习：开发一个教务管理系统，在该系统中可以维护和管理学员的成绩信息，具体需求如下。
1.添加学生信息:根据提示录入学生姓名、语文、数学、英语成绩，录入完成保存到系统中。
2.修改学生信息，要求输入要修改的学生姓名，然后再提示输入语文、数学、英语成绩，输入完成后修改学员信息。
3.删除学生信息：要求输入删除的学生姓名，根据姓名删除学生信息。
4.查询学生信息：要求输入要查询的学生姓名，根据姓名查询学生信息并输出。
5.列出所有学生：遍历所有学生信息并输出。
6.统计班级成绩：统计班级语文、数学、英语的最高分、最低分、平均分、以及语文、数学、英语最高分和最低分的学员姓名。
7退出系统
"""
student = {}

num = ("""
#############欢迎进入教务系统#############
#                                  1.录入学生信息                                      #
#                                   2.修改学生信息                                     #
#                                    3.删除学生信息                                    #
#                                  4.查询学生信息                                     #
#                                    5.列出学生信息                                   #
#                                   6.统计班级成绩                                    #
#                                    7.退出系统                                             #
########################################
""")
print("您已进入教务系统")
while True:
    print(num)
    choice = input("请选择要执行的操作（1-7）")
    match choice :
        case "1":#录入学生信息
            student_name = input("请输入学生姓名：")
            student_chinese = int(input("请输入语文成绩："))
            student_math = int(input("请输入数学成绩"))
            student_english = int(input("请输入英语成绩"))
            if student_name in student:
                print("以录入学生信息，请勿重复录入")
            else:
                student[student_name] = {"chinese": student_chinese, "math": student_math, "english": student_english}
                print("学生信息已录入系统")

        case "2":       #修改学生信息
            student_name = input("请输入修改的学生姓名：")
            if student_name not in student:
                print("抱歉未查询到学生信息请录入")
                continue
            student_chinese = int(input("请输入语文成绩："))
            student_math = int(input("请输入数学成绩"))
            student_english = int(input("请输入英语成绩"))
            student[student_name] = {"chinese": student_chinese, "math": student_math, "english": student_english}
            print("学生信息已修改")
        case "3":#删除学生信息
            student_name = input("请输入要删除的学生姓名")
            if student_name not in student:
                print("未查询到学生信息请重新输入")
            else :
                del student[student_name]
        case "4":#查询学生信息
            student_name = input("请输入要查询的学生姓名：")
            if student_name not in student:
                print("未查询到该学生信息")
            else:
                info = student[student_name]
                print(f"学生姓名：{student_name}")
                print(f"语文成绩：{info['chinese']}")
                print(f"数学成绩：{info['math']}")
                print(f"英语成绩：{info['english']}")
        case "5":#遍历学生信息
            for k,v in student.items():
                print(f"学生姓名：{k}，\t语文成绩:{v["chinese"]},\t数学成绩:{v["math"]},\t英语成绩:{v["english"]}")
        case "6":
            if not student:
                print("暂无学生信息，无法统计")
                continue

            # 提取成绩列表
            ch_scores = [s["chinese"] for s in student.values()]
            ma_scores = [s["math"] for s in student.values()]
            en_scores = [s["english"] for s in student.values()]

            # 计算平均分
            ch_avg = sum(ch_scores) / len(ch_scores)
            ma_avg = sum(ma_scores) / len(ma_scores)
            en_avg = sum(en_scores) / len(en_scores)

            # 找极值学生（只找一个，不处理并列）
            ch_max_student = max(student.items(), key=lambda x: x[1]["chinese"])[0]
            ch_min_student = min(student.items(), key=lambda x: x[1]["chinese"])[0]
            ma_max_student = max(student.items(), key=lambda x: x[1]["math"])[0]
            ma_min_student = min(student.items(), key=lambda x: x[1]["math"])[0]
            en_max_student = max(student.items(), key=lambda x: x[1]["english"])[0]
            en_min_student = min(student.items(), key=lambda x: x[1]["english"])[0]

            print("\n======= 班级成绩统计 =======")
            print(
                f"语文：最高分 {max(ch_scores)}（{ch_max_student}），最低分 {min(ch_scores)}（{ch_min_student}），平均分 {ch_avg:.2f}")
            print(
                f"数学：最高分 {max(ma_scores)}（{ma_max_student}），最低分 {min(ma_scores)}（{ma_min_student}），平均分 {ma_avg:.2f}")
            print(
                f"英语：最高分 {max(en_scores)}（{en_max_student}），最低分 {min(en_scores)}（{en_min_student}），平均分 {en_avg:.2f}")

        case "7":
            print("您已退出教务系统")
            break
        case _:
            print("输入无效重新输入")
            continue


