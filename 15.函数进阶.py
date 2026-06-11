# #-------------------------  函数 - 不定长参数(位置参数 *args --> 元组)------------------------------
# # 需求：根据传入的这批数据，计算这批数据的最小值、最大值、平均值
# def calc_date(*arge):
#     """
#
#     :param arge: 不定长参数（位置参数）
#     :return: 返回最大值、最小值、平均值
#     """
#     max_date = max(arge)
#     min_date = min(arge)
#     avg_date = sum(arge)/len(arge)
#     return max_date, min_date, round (avg_date,2)
#
# print(calc_date(1,7,78,999,15,28,30))
from unittest import result

# #-------------------------  函数 - 不定长参数(关键字参数 *kwargs --> 字典)------------------------------
# def calc_date(*arge,**kwarge):
#     """
#
#     :param arge: 关键字参数
#     :param kwarge: 字典参数
#     :return: 返回最高值，最低值，平均值
#     """
#     max_date = max(arge)
#     min_date = min(arge)
#     avg_date = sum(arge) / len(arge)
#     if kwarge.get("round")  is not None:
#         avg_date = round(avg_date, kwarge.get("round"))
#     if kwarge.get("print") :
#         print(f"最高值{max_date},最低值{min_date},平均值{avg_date}")
#     return max_date, min_date, avg_date
#
#
# print(calc_date(1, 7, 78, 999, 15, 28, 30,round = 3,print = True))

# #可以定义函数为参数
# def add(x,y):
#     return x+y
# def subtract(x,y):
#     return x-y
# def multiply(x,y):
#     return x*y
# def divide(x,y):
#     return x/y
# def calc(x,y,oper):#oper 是函数
#     return oper(x,y)
#
# print(calc(10,20,add))


# #匿名函数
# out_line =  lambda : print("____________________")
# out_line()
# add = lambda x,y: x+y
# print(add(100,300))
#
# # 练习：完成如下列表中的排序操作，按照每一个元素的字符个数，从小到大排序；
# date_list = ["c++", "c", "python", "jack", "PHP", "jave", "Go", "javaScript", "Rust"]
# date_list.sort(key= lambda i : len(i))#匿名函数典型应用场景
# print(date_list)


# #案例1:计算n的阶乘
# # 递归调用(先层层递进，再逐层回归)：在函数中自己调用自己的情况 -------一定要有终结点
# def jc(n) :
#    if n == 0 :
#        return 1
#    else :
#        return n * jc(n-1)
# result = jc(10)
# print(result)


#案例2:定义一个函数，用户根据传入的一批商品信息（商品名、价格、数量）、优惠（优惠卷、积分抵扣）、运费信息计算订单的总金额。
# 具体规则如下：
# 优惠卷需要商品金额满5000才可以使用，且优惠卷金额不能超过商品总价。
# 积分抵扣需要商品金额满5000才可以使用，100积分抵扣1元（且抵扣金额不能超过商品总价，积分只能整百抵扣）
def calc_order_cost(*args:tuple[str,float,int],coupon = 0, score = 0, express = 0) -> float:
    """

    :param args: 商品信息（商品名，价格，数量）
    :param coupon: 优惠卷
    :param score: 积分
    :param express: 运费
    :return: 订单金额
    """
    total_price = [goods[1]*goods[2] for goods in args]
    total_cost = sum(total_price)

    if total_cost >= 5000 and coupon > 0:
        total_cost -= coupon

    if total_cost >= 5000 and score//100 <= total_cost:
        total_cost -= score//100

    total_cost -= express
    return total_cost
total = calc_order_cost(("pocket4",2999,1),("macbook",19999,1),("iphone17pro max",10099,1),coupon = 5000, score=10000, express=199)
print(total)

