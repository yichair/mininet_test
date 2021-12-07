def A(fn):
    print("C语言中文网")
    fn()
    print("http://c.biancheng.net")
    return "装饰器函数的返回值"
@A
def B():
    print("funB():")


# 装饰器，相当于有一行代码B = A(B)
# 输出：
# C语言中文网
# funB():
# http://c.biancheng.net