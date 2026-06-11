# # 定义类 ----------> 不推荐 动态的为对象添加属性
# class Car :
#     pass
# #创建对象
# c1 = Car()
# c1.color = "green"
# c1.brand = "LiXiang"
# c1.name = "M8"
# c1.price = 680000
#
# print(c1.color)
# print(c1. __dict__)#会将对象中所有属性以字典形式输出出来


# # 定义类
# class Car:
#     #__init__方法是初始化的方法，会在对象创建时自动调用，可以在该方法中为对象设置对应属性
#     #self : 是第一个参数，表示当前所创建出来的实例对象
#     def __init__(self, color, brand,name,price):
#         self.color = color
#         self.brand = brand
#         self.name = name
#         self.price = price
#         print("Car 类型的对象初始化完毕，对象属性已经添加完毕。")
# #创建对象
# c1 = Car("绿色", "理想","M8", 688000)
# print(c1.__dict__)

#-----------------------------------------定义类实例方法------------------------------------
# class Car:
#     def __init__(self, color, brand, name, price):
#         self.color = color
#         self.brand = brand
#         self.name = name
#         self.price = price
#         print("Car 类型的对象初始化完毕，对象属性已经添加完毕。")

#     def running(self):
#         print(f"{self.brand},{self.name}正在高速行驶中·······")
#
#     def total_cost(self, discount, rate):
#         """
#         计算车子的最终购置费用
#         :param discount:折扣
#         :param rate:税率
#         :return:提车总费用
#         """
#         return self.price * discount + rate * self.price
#
# #测试
# c1 = Car("绿色", "理想","M8", 688000)
#
# # #调用对象中的方法
# # c1.running()
# # total = c1.total_cost(discount=0.75, rate=0.1)
# # print(f"购车总费用{total}")
#     def __str__(self):
#         return f"{self.color} {self.brand} {self.name} {self.price}"
#     def __eq__(self, other):
#         return self.color == other.color and self.brand == other.brand and self.name == other.name and self.price == other.price
#     def __lt__(self, other):
#         return self.price < other.price
# #魔法方法
# c1 = Car("绿色","理想", "M8", 880000)
# print(c1)
# c2 = Car("黑色", "理想", "M8", 800000)
# print(c2)
#
# print(c1 == c2)
# print(c1> c2)

# -----------------------------------实例属性、类属性----------------------------------------
# class Car:
#     wheel = 4 #轮胎数量
#     tax_rate = 0.1 #税率
#     def __init__(self, color, brand, name, price):
#         self.color = color
#         self.brand = brand
#         self.name = name
#         self.price = price
#         print("Car 类型的对象初始化完毕，对象属性已经添加完毕。")
#         def running(self):
#             print(f"{self.brand},{self.name}正在高速行驶中·······")
#
#         def total_cost(self, discount, rate):
#             """
#             计算车子的最终购置费用
#             :param discount:折扣
#             :param rate:税率
#             :return:提车总费用
#             """
#             return self.price * discount + rate * self.price
#
#
# c1 = Car("绿色", "理想", "M8", 880000)
# print(c1.tax_rate)
# c2 = Car("黑色", "理想", "M8", 800000)
# print(c2)



# # 案例
# """采用面向对象编程的思想，完成教务系统的开发。教务系统可以管理在校学生的成绩信息，通过控制台菜单与用户交互，具体功能如下
# 1.添加学生成绩：根据输入的学生姓名、语文成绩、数学成绩、英语成绩记录在系统中
# 2.修改学生成绩：据输入的学生姓名，修改对应的学生成绩
# 3.删除学生成绩：根据输入的学生姓名，删除对应的学生成绩
# 4.查询指定学生成绩：根据输入的学生姓名，查找对应的学生成绩，并输出
# 5.展示全部学生成绩：展示出系统中所有的学生成绩"""
# from unittest import case
# class StudentScores :
#     def __init__(self, name, chinese_score,math_score,english_score) :
#         self.name = name
#         self.chinese_score = chinese_score
#         self.math_score = math_score
#         self.english_score = english_score
#     def __str__(self):
#         return f"姓名：{self.name} | 语文成绩：{self.chinese_score} | 数学成绩：{self.math_score} | 英语成绩：{self.english_score} | 总成绩：{self.chinese_score + self.math_score + self.english_score}"
#     def update_score(self,chinese_score = None,math_score = None,english_score = None) :
#       if chinese_score is not None :
#           self.chinese_score = chinese_score
#       if math_score is not None :
#           self.math_score = math_score
#       if english_score is not None :
#           self.english_score = english_score
# class EduManagement:
#     system_version = "1.0"
#     system_name = "教务系统"
#
#     def __init__(self):
#         self.student_scores = []
# #添加学生成绩
#     def add_student(self) :
#         name = input("请输入学生姓名：")
#         for s in self.student_scores :
#             if s.name == name :
#                  print("该学生信息已存在，请重新录入！")
#                  return
#
#         chinese = int(input("请输入语文成绩："))
#         math = int(input("请输入数学成绩："))
#         english = int(input("请输入英语成绩："))
#         if 0 <= chinese <= 100 and 0 <= math <=100 and 0 <= english <= 100:
#             stu = StudentScores(name,chinese,math,english)
#             self.student_scores.append(stu)
#             print("学生信息添加成功！！！")
#         else:
#             print("输入错误，请输入0～100之间数字！")
#
# #修改学生成绩
#     def update_student(self) :
#        name =  input("请输入要修改的学生姓名：")
#        for s in self.student_scores :
#            if s.name == name :
#                print(f"修改前学生信息{s}")
#                chinese = int(input("请输入修改后语文成绩："))
#                math = int(input("请输入修改后数学成绩："))
#                english = int(input("请输入修改后英语成绩："))
#                if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
#                    s.update_score(chinese,math,english)
#                    print(f"修改成功，修改后的成绩：{s}")
#                    return
#                else:
#                    print("输入错误，请输入0～100之间数字！")
#                    return
#        print("未找到学生信息！！")
#
#
#
# #删除学生成绩
#     def delete_student(self) :
#         name = input("请输入要修改的学生姓名：")
#         for s in self.student_scores :
#             if s.name == name :
#                 self.student_scores.remove(s)
#                 print("成功删除信息！")
#                 return
#         print("未找到该学生信息！！")
#
# #查询指定学生信息
#     def query_students(self) :
#         name = input("请输入要查询的学生姓名：")
#         for s in self.student_scores:
#             if s.name == name:
#                 print(f"学生信息：{s}")
#                 return
#         print("未找到该学生信息！！")
#
# #查询所有学生信息
#     def list_students(self) :
#         for s in self.student_scores:
#             print(s)
#
# #运行系统
#     def run(self) :
#         print(f"欢迎进入教务系统，版本V{EduManagement.system_version}")
#         while True :
#             num = ("""
#             ############################################
#             #                                    欢迎进入教务系                                               #
#             #                                    请选择您要处理的事物                               #
#             #                                    1.添加学生信                                                   #
#             #                                    2.修改学生信                                                   #
#             #                                    3.删除学生信                                                   #
#             #                                    4.查询学生信                                                   #
#             #                                    5.获取全部学生信息                                   #
#             #                                    6.退出系统                                                       #
#             ###########################################
#             #  """)
# #             print(num)
#             choice = input("请选择要执行的操作，1-6")
#             match choice :
#                 case "1" :
#                     self.add_student()
#                 case "2" :
#                    self.update_student()
#                 case "3":
#                     self.delete_student()
#                 case "4" :
#                    self.query_students()
#                 case "5" :
#                    self.list_students()
#                 case "6" :
#                     print("成功退出教务系统 ，感谢使用！")
#                     break
#                 case _ :
#                     print("输入错误请选择1-6之间")


#练习
# - 采用面向对象的编程思想，开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。
# 系统使用自定义对象存储商品数据，通过控制台菜单与用户交互。具体功能如下：
#

class Item:

    def __init__ (self,name,quan,unit_price,total_price):
        self.name = name
        self.quan = quan
        self.unit_price = unit_price
        self.total_price = total_price
    def __str__(self):
        item = f"商品名称：{self.name} ｜商品数量：{self.quan}｜商品单价： {self.unit_price}｜商品总价： {self.total_price}"
        return item
    #修改商品
    def update_total_price(self,quan = None,unit_price = None,total_price = None):
        if quan is not  None:
             self.quan = quan
        if unit_price is not  None:
             self.unit_price = unit_price
        if total_price is not  None:
            self.total_price = total_price


class ShoppingCar:
    system_version = "1.0"
    system_name = "购物车系统"
    def __init__(self):
        self.items = []
# 1. 添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
    def add_item(self):
        name =  input("请输入商品名称：")
        for i in self.items:
            if i.name == name:
                print("该商品已存在，请勿重新添加")
                return
        quan = int( input("请输入商品数量："))
        unit_price = float( input("请输入商品单价"))
        total_price = quan * unit_price
        if quan>=0 and unit_price>=0 :
            it = Item(name,quan,unit_price,total_price)
            self.items.append(it)
            print(f"商品添加成功：{it}")
        else:
            print("输入错误，请重新输入！")

# 2. 修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
    def change_item(self):
        name = input("请输入要修改的商品名称：")

        for i in self.items:
            if i.name == name:
                print(f"商品修改前信息：{i}")
                quan = int(input("请输入商品数量："))
                unit_price = float(input("请输入商品单价"))
                total_price = f"商品总价：{quan * unit_price}"
                if quan >= 0 and unit_price >= 0:
                    i.update_total_price(quan,unit_price,total_price)
                    print("修改商品成功！")
                    print(f"修改后的商品信息：{i}")
                    return
                else :
                    print("输入错误请从新输入！")
                    return
        print("未查询到该商品！")

# 3. 删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
    def delete_item(self):
        name = input("请输入要删除的商品：")
        for i in self.items:
            if i.name == name:
                self.items.remove(i)
                print("删除成功！！")
                return
        print("未找到商品信息！！！")
# 4. 查询购物车：将购物车中的商品信息展示出来，格式为：“商品名称：×××，商品价格：×××，商品数量：×××”。
    def query_item(self):
        for i in self.items:
                print(i)



# 5. 退出购物车
    def run(self):
        print(self.system_version)
        print(self.system_name)
        while True:
            print("#####################################")
            print("#                       1.添加商品信息                                        #")
            print("#                       2.修改商品信息                                        #")
            print("#                       3.删除商品信息                                        #")
            print("#                       4.查询所有商品信息                              #")
            print("#                       5.退出系统                                                  #")
            print("#####################################")
            print()
            choice = input("请输入您要执行的操作，1-6:")

            match choice:
                case "1":
                    self.add_item()
                case "2":
                    self.change_item()
                case "3":
                    self.delete_item()
                case "4":
                    self.query_item()
                case "5":
                    print("成功退出购物系统 ，感谢使用！")
                    break
                case _:
                    print("输入错误，请输入1-6")








if __name__ == '__main__':
    # edu_management = EduManagement()
    # edu_management.run()
    try:
        shopping_car = ShoppingCar()
        shopping_car.run()
    except Exception as e :
        print("输入错误，请联系管理员，错误信息",e)