try:
    msg = input("请输入：")
    int(msg)
except Exception as e:
    print(e)