# 1.导入模块 ----------> 调用方式：模块名.功能名/别名.功能名

# import random
# for i in range(100):
#     print(random.randint(1,100))
#
# import random as rd
# for i in range(100):
#     print(rd.randint(1,100))


# 2.导入模块中的功能   from····import····  ----> 调用方式：功能名/别名

# from random import randint
# for i in range(100):
#     print(randint(1,100))

# from random import randint as  rd
# for i in range(100):
#     print(rd(1,100))

# from random import *
# for i in range(100):
#     print(randint(1,100))

nums = [1,2]
res = nums.append()
ok = res is None
print(nums,ok)