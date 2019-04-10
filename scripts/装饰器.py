import time

def timer(func):
    def wrapper():
        start_time = time.time()
        res = func()
        stop_time = time.time()
        print("函数运行时间是：%s"  %(stop_time - start_time))
        return res
    return wrapper
@timer
def test():
    time.sleep(3)
    print("test函数运行完毕")
    return '123'
res=test()
print(res)