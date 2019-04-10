#把函数当作参数传给另一个函数
# def foo(n):
#     print(n)
#
# def bar(name):
#     print("my name is %s",name)
#
# foo(bar("alex"))

def foo():
    print("from foo")
    return foo
foo()