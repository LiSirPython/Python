import pymysql

#数据库信息
conn = pymysql.connect(host = '172.16.6.128',port = 3306, user = 'root', passwd = '123456',db = 'test')
#获取游标，相当于MySQL命令行里的光标
#cursor默认返回结果是元组的形式
cursor = conn.cursor()

#cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)可以设置查询结果为字典形式


#执行MySQL命令，execute()方法会有返回结果，可以根据结果判断是否执行成功
sql = "create table test(id INT,name VARCHAR (20))"
cursor.execute(sql)
cursor.execute("INSERT INTO test VALUES (1,'alex'),(2,'alvin')")
ret = cursor.execute("select * from test")   #返回查询到的行数
print(ret)

#显示查询结果，fetchone()显示一行，fetchone()显示所有结果，fetchmany(参数)显示指定行数查询结果
print(cursor.fetchone())  #显示一行
# print(cursor.fetchmany(2))  #显示两行
# print(cursor.fetchall())  #显示所有查询结果

cursor.scroll(1,mode="relative")  #移动光标的方法，1是正数是向下移动一行，负数是向上移动，mode="relative"针对当前相对位置
                                    #mode="absolute"取绝对位置



#插入数据必须使用commit()方法提交才能生效，创建表不需要
conn.commit()
#关闭游标
cursor.close()
#关闭MySQL连接
conn.close()