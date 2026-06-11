# find() 在字符串中查找子串，返回第一次出现的索引位置，找不到返回-1  样例:s.find("python")
# count() 统计子串在字符中出现的次数 样例：s.count("H")
# upper() 将字符串中的所有字母转换为大写 样例：s.upper()
# lower() 将字符串中的所有字母转换为小写 样例： s.lower()
# split() 将字符串按指定分隔符分割成列表 样例：s.split("  ")
# strip() 去除字符串两端的空白字符或指定字符：s.strip()/s.strip("*")
# replace() 将字符串中的指定子串替换为新的子串 样例： s.replace("H" , "C")
# startswith() 检查字符串是否以指定子串开头，返回布尔值 样例：s.starwith("P")

# # 案例1：邮箱格式验证：用户输入一个邮箱，验证邮箱格式是否正确(包含一个@和至少一个.)如果输入正确输出“邮箱格式正确”否则输出“邮箱格式错误”
# emails = input("请输入邮箱:")
# if emails.count("@") == 1  and emails.count(".") >= 1:
#     print("邮箱格式正确")
# else:
#     print("邮箱格式错误")
#
# # 方法2: in 判断子串是否在字符串中
# emails = input("请输入邮箱:")
# if "@"in emails  and "."in emails:
#     print("邮箱格式正确")
# else:
#     print("邮箱格式错误")

# # 练习1:输入一段字符串，判断该字符串是否回文（两边对称）
# i = "黄山落叶松叶落山黄"
# s= "上海自来水来自海上"
# if i == i [::-1]:
#     print(f"‘{i}’，是回文")
# if s == s [::-1]:
#     print(f"‘{s}’，是回文")

# 练习2:将用户输入的10个字符串，反转后全部转为大写，然后记录在列表中，最后将列表内容遍历出来。
num = input("请输入英文内容（10个字符串）")
s = num . upper()
s.split("--")
for i in s:
    print(f"字符:{i}")
print()
