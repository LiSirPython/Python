import pymysql

#添加数据

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='yyy')

cursor = conn.cursor()


try:
    insertSQL0="INSERT INTO ACCOUNT2 (name,balance) VALUES ('oldboy',4000)"
    insertSQL1="UPDATE account2 set balance=balance-30 WHERE name='yuan'"
    insertSQL2="UPDATE account2 set balance=balance+30 WHERE name='xialv'"

    cursor = conn.cursor()

    cursor.execute(insertSQL0)
    conn.commit()

    cursor.execute(insertSQL1)
    raise Exception          #当程序出现错误，python会自动引发异常，也可以通过raise显示地引发异常。一旦执行了raise语句，raise后面的语句将不能执行
    cursor.execute(insertSQL2)
    cursor.close()
    conn.commit()  #Commit 提交事务，提交未存储的事务

except Exception as e:

    conn.rollback()  # Rollback 回滚事务,即撤销指定的sql语句(只能回退insert delete update语句)，回滚到上一次commit的位置
    conn.commit()


cursor.close()
conn.close()


#Pymysql本身就是基于MySQL事务来进行操作的
# 事务指逻辑上的一组操作，组成这组操作的各个单元，要不全部成功，要不全部不成功。
#
# 数据库开启事务命令
#
# --        start transaction 开启事务
# --        Rollback 回滚事务,即撤销指定的sql语句(只能回退insert delete update语句)，回滚到上一次commit的位置
# --        Commit 提交事务，提交未存储的事务
# --
# --        savepoint 保留点 ，事务处理中设置的临时占位符 你可以对它发布回退(与整个事务回退不同)