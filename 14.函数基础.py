# #注意：函数定义的时候并不会执行，只有调用函数的时候，函数体的逻辑才会执行；函数必须先定义，后调用。
# #函数定义
# def out_line() :
#     print("____________________")
#     print("_____________________")
#
# out_line()
# out_line()


# #函数的参数与返回值
# #计算圆的面积----半径
# def circle_area(r):
#     area = 3.14*r*r
#     return area
#
# c_area = circle_area(8)
# print(c_area)
#
# # #计算长方形的面积---长*宽
# def rectangle_area(l,w):
#     """
#     根据长方形的长和宽求长方形的面积
#     :param l: 长方形长
#     :param w: 长方形宽
#     :return: 长方形的面积
#     """
#     area = l * w
#     return area
# re_area = rectangle_area(2,4)
# print(re_area)
#
# #计算圆的面积与周长------> 有多个返回值 ， 来分割------->多个返回值封装在元组之中
# def circle_area_len(r):
#     """
#     根据圆的半径求圆的面积和周长
#     :param r: 圆的半径
#     :return: 圆的面积，圆的周长
#     """
#     return round(3.1415926525* r ** 2,1), round(2 *3.1415926535 * r,1)
# area_len = circle_area_len(20)
# print(area_len)
# area,len = circle_area_len(20)#解包
# print(area)
# print(len)
# # help(circle_area_len)


# 案例；
#     1.定义一个函数；根据传入的底和高，计算三角形的面积的函数（三角形面积=底*高/2）
def triangle_area(s,h) :
    """

    :param s: 长方形的底
    :param h: 长方形的高
    :return: 计算长方形的面积
    """
#     return s * h/2
# area = triangle_area(10,5)
# print(area)

#     2.定义一个函数：计算传入的字符串中，元音字母的个数（元音字母为 aeiouAEIOU）
def str_num (s):
    """
    :param s: 字符串
    :return: 计算输入字符串元音字母数量
    """
    num =0
    for k in s:
        if k in "aeiouAEIOU" :
            num +=1
    return num
print(str_num("hello world , hello python"))

#     3.定义一个函数：计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分（保留1位小数）
def calc_score(score_list):
    """

    :param :列表
    :return:最大值 最小值 平均数
    """
    max_s = max(score_list)
    min_s = min(score_list)
    avg_s = round(sum(score_list)/len(score_list),1)
    return max_s, min_s, avg_s

s_list = [589,609,605,313,541,379,640,710]
max_score, min_score_s, avg_score = calc_score(s_list)
print("最高分：",max_score)
print("最低分：",min_score_s)
print("平均分：",avg_score)

# 练习1.定义一个函数，根据传入的分数，计算对应的分数等级并返回
def calculate_score(s):
    """

    :param s: 分数
    :return: 计算评级

    """
    grand = str()
    if s >= 90:
        grand = "A"
    elif s >= 75:
        grand = "B"
    elif s>=60:
        grand = "C"
    else:
        grand = "D"
    return grand

print(calculate_score(20))

# 练习2:定义一个函数，用于判断一个字符串是否是回文，返回布尔值
def condition(i):
    """

    :param i: 一段文字
    :return: true or  false
    """
    if i == i[::-1]:
        return True
    else:
        return False
print(condition("风萧萧兮易水寒"))
print(condition("黄山落叶松叶落山黄"))

# 练习3:定义一个函数，完成时间转换功能，将传入的秒转换为小时、分钟、秒

def convert_seconds(t):
        """
        将秒数转换为小时、分钟、秒
        :param t: 总秒数（整数）
        :return: 格式化的字符串，如 "X小时Y分钟Z秒"
        """
        hours = t // 3600  # 计算小时数
        remainder = t % 3600  # 剩余秒数（不足1小时的部分）
        minutes = remainder // 60  # 计算分钟数
        seconds = remainder % 60  # 计算秒数
        return f"{hours}小时{minutes}分钟{seconds}秒"

    # 测试示例
print(convert_seconds(56))  # 输出：1小时1分钟5秒

# 练习4：定义一个函数：根据输入的三角形三个边长，判定三角形的类型（等边，等腰，普通，或者不构成三角形）。
def triangle (l,w,h):
    """

    :param l: 三角形的边
    :param w: 三角形的边
    :param h: 三角形的边
    :return: 判断三角形类型
    """
    sides = [l,w,h]
    sides.sort()
    a, b, c = sides[0],sides[1],sides[2]
    if a+b >c and a>0 and b>0 and c>0:
        if l == w == h:
            return "等边三角形"
        if l== w or w == h or h==l:
            return "等腰三角形"
        else:
            return "普通三角形"
    else:
        return "不构成三角形"

print(triangle(2,4,2))