"""
    1. Create a mysql table ai_nn_emp to contain empno,name,deptcode,desig,salary and insert some records(10)


create table ai_13_emp(deptno int NOT NULL,dept_name varchar(20) NOT NULL,dept_location,PRIMARY KEY (deptno));
"""
# importing packages
import MySQLdb as db
import pandas as pd

con = None
dept=list(["Head Office", "R&D","Data Analytics","Data Science Lab","Project X","Lingusitics Dept","Embedded Designs Lab","Data Centre","Data Centre","Advertising","HR"])
loc=list(["Main","Block 1","Block 2","Block 3","Classified","Block 4","Block 5","Block 6","Block 7","Block 8","Block9"])
try:
    con = db.connect("127.0.0.1","aravind","sql91011","db")
    cur = con.cursor()
    for i in range(10):
        sql = "insert into ai_13_dept values(%s,%s,%s)",(str(i+2000),dept[i],loc[i])
        cur.execute(*sql)
    con.commit()

except Exception ,e :
    print e
finally:
    con.close()
