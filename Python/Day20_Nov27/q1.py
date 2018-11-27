import numpy as np
dt1=np.dtype([('ename','S20'),('eno','i8'),('edesign','S10'),('esalary','f8'),('ephno','S15')])
alf=np.loadtxt('emp.csv',delimiter=",",dtype=dt1)
print "All the records : \n ",alf
print "\n Names of officers : \n ",alf[alf['edesign']=='officer']['ename']
print "\n Scientist Records : \n ",alf[alf['edesign']=='scientist']
print "\n Total Salary : \n",alf['esalary'].sum()
print "\n Average Salary of Engineers : \n",alf[alf['edesign']=='engineer']['esalary'].mean()
print "\n Emplyees in Acending order of salary : \n ",np.sort(alf,order='esalary')
print "\n Emplyees in Acending order designation of salary : \n ",np.sort(np.sort(alf,order='edesign'),order='esalary')
print "\n Lowest salary for Scientist Designation : \n ",np.sort(alf[alf['edesign']=='scientist'],order='esalary')[0]
alf1=alf[alf['edesign']=='scientist']
print "\n Employees who are scientists with lowest salary : \n",alf1[alf1['esalary']==alf1['esalary'].min()]
