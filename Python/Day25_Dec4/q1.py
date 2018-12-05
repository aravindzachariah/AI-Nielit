import pandas as pd
import re

#Function to remove Non-Numeric Values
def Rep(n):
	return re.sub('[^0-9\.]','',str(n))

#Question 1
ef1=pd.read_csv("emp.csv",header=None)
ef1.columns="Ename EmpNo EDesig ESalary EPhNo".split()

#Question 2
ef2=ef1.copy()
ef2['EPhNo']=ef2['EPhNo'].apply(Rep)
print ef2,"\n"

#Question 3
writer=pd.ExcelWriter("empx.xlsx")
et2=ef2.drop(['EmpNo','EPhNo'],axis=1)
et2.to_excel(writer,sheet_name="salary")

#Question 4
ef2.drop(['EmpNo','EDesig','ESalary'],axis=1).to_excel(writer,sheet_name="phone")
writer.save()

#Question 5
ef3=ef2.set_index(['EDesig','EmpNo'])
print ef3,"\n"

#Question 6
ef4=ef3.sort_index(level='EDesig')
print ef4,"\n"

#Question 6.1
print ef4.loc['scientist',:],"\n"

#Question 6.2
print "Average Salary of Engineers : ",ef4.loc['engineer',:]['ESalary'].mean(),"\n"

#Question 6.3
print "Minimum Salary of Scientist : ",ef4.loc['scientist',:]['ESalary'].min(),"\n"

