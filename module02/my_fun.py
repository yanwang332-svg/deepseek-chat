# __all__是一个模块级别的特殊变量，用于指定form模块名inport * 可以导入的函数与自变量（*通配了哪些功能）

# 常量（不会变化的数据，通常的名称全部大写）
PI = 3.1415926
NAME = "王琰"


# 函数
def log_separator1():
    print("-" * 30)
def log_separator2():
    print("*"*30)
def log_separator3():
    print("#"*30)


# 测试函数
#__name__:python中的内置变量，表示的当前模块的名字（直接运行当前模块，name的值为__main__,当该模块被导入时，__name__的值就是模块名）
#执行当前文件，则会执行以下代码，当被导入模块时，不会执行以下代码。
if __name__ == '__main__':
    log_separator1()
    log_separator2()
    log_separator3()