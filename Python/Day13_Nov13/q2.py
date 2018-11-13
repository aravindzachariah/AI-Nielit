
import pandas as pd
import xml.dom.minidom as dm
X=pd.read_csv("emp.csv")
X=X.as_matrix()
import MySQLdb as db
try:
	con=db.connect('127.0.0.1','ai','ai','ai')
	cur=con.cursor()
	for i in range(4):	
		qsl="insert into emp_ai13 values(%s,%s,%s,%s)",(X[i,0],X[i,1],X[i,2],X[i,3])
		res=cur.execute(*qsl)
		con.commit()
except Exception,args:
	print args
else:
	print "Sucess"
