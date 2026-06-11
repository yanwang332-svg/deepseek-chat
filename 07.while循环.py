# 案例1:计算1-100之间所有的偶数和
num = 0
total = 0
while num <= 100 :
    if num % 2 == 0:
        total += num
    num += 1
else:
    print(f"所有偶数和为：{total}")

