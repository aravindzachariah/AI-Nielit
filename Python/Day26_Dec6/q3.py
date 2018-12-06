"""
create table ai_13_emp_dept(empno int NOT NULL,name varchar(20) NOT NULL,dep_name varchar(20),salary int,PRIMARY KEY (empno));

"""
import sqlalchemy.sql
import MySQLdb as my
import pandas as pd
import numpy as np
from sqlalchemy import create_engine as ce
con=my.connect('localhost','aravind','sql91011','db')
df1=pd.read_sql("select * from ai_13_emp",con)
df2=pd.read_sql("select * from ai_13_dept",con)
print df1
df3=pd.merge(df1,df2,left_on='deptcode',right_on='deptno')[['empno','name','dep_name','salary']]
print df3
con=ce('mysql://bda:bda@localhost/db')
df3.to_sql("ai_13_emp_dept",con)
