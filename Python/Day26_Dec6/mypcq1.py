"""
    1. Create a mysql table ai_nn_emp to contain empno,name,deptcode,desig,salary and insert some records(10)


create table ai_13_emp(empno int NOT NULL,name varchar(20) NOT NULL,deptcode int,desig varchar(20),salary int,PRIMARY KEY (empno));
"""
# importing packages
import MySQLdb as db
import pandas as pd

con = None
names=list(["Tom", "Raj","Tony","Shibin","Aravind","Akshey","Varun","Amel","Nizam","Roy","Rahul"])
desig=list(["Engineer","Scientist","Engineer","Scientist","Officer","Scientsit","Officer","Engineer","Scientist","Officer","Engineer"])
slry=[100000,60000,30000,70000,50000,20000,60000,70000,50000,60000,70000]
try:
    con = db.connect("127.0.0.1","aravind","sql91011","db")
    cur = con.cursor()
    for i in range(10):
        sql = "insert into ai_13_emp values(%s,%s,%s,%s,%s)",(str(i+100),names[i],str(i+2000),desig[i],str(slry[i]))
        cur.execute(*sql)
    con.commit()

except Exception ,e :
    print e
finally:
    con.close()
