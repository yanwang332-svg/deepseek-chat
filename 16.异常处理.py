def fun1() :
    print("fun1~~~~run~~")
    fun2()
def fun2() :
    print("fun2~~~~run~~")
    fun3()
def fun3() :
    print("fun3~~~~run~~")
    print(my_colour)

if __name__ == '__main__':
    try:
        fun1()
    except Exception as e :
        print("输入错误，请联系管理员，错误信息：",e)



