# # 案例：实现一个计算器，可以实现 + - * / 运算， 用户输入需要运算的两个数及运算符之后，就可以进行计算。
# nub1 = int(input("请输入第一个数"))
# nub2 = int(input("请输入第二个数"))
# symbol = input("请输入运算符（+ - * /）")
# match symbol:
#     case "+":
#         print(f"{nub1} + {nub2} = {nub1 + nub2}")
#     case"-" :
#         print(f"{nub1} - {nub2} = {nub1 - nub2}")
#     case "*" :
#         print(f"{nub1} * {nub2} = {nub1 * nub2}")
#     case "/"if nub2 != 0 :#if 条件成才会匹配case
#         print(f"{nub1} / {nub2} = {nub1 / nub2}")
#     case _ :
#         print("暂不支持该符号！！！！")

# # 练习：请编写一个游戏角色移动系统，根据玩家输入的不同指令，控制游戏角色执行的相应动作（输出控制台）
# 上/w/W   角色向上移动
# 下/s/S      角色向下移动
# 左/a/A     角色向左移动
# 右/d/D     角色向右移动
# 跳/“ ”（空格） 角色跳跃
# 攻击/j/J   角色发动攻击
# 退出/esc/ESC  角色退出游戏
game = input("输入操作指令:")
match game:
    case "上"|"w" |"W" :
        print("角色向上移动")
    case "下" | "s" | "S" :
        print("角色向下移动")
    case "左" | "a" | "A" :
        print("角色向左移动")
    case    "右" | "d" | "D" :
        print("角色向右移动")
    case "跳" | " " :
        print("角色跳跃")
    case "攻击" | "e" | "E" :
        print("角色攻击")
    case "退出" | "esc" | "ESC" :
        print("退出游戏")
    case _ :
        print("输入无效")