for i in range(1,10):       #乘数
    for j in range(1,i+1):  #被乘数
        print("%d*%d=%d\t" %(j,i,i*j),end="")  #/t空格，end作用是print输出不换行
    print()   #循环完成以后换行