import numpy as np
o=list('abcdef')
k='a'
dt1=np.dtype([('ename','S20'),('eno','i8'),('edesign','S10'),('esalary','f8'),('ephno','S10')])
while(k in o):
	print "\na)Initialize \nb)Add New record \nc)Delete Record \nd)Display details by name \ne)Display Summary \nf)Save all \ng)Exit \n"
	k=raw_input("Enter Option: ")
	if k=='a':
		data1=np.loadtxt('emp.csv',delimiter=",",dtype=dt1)
	elif k=='b':
		n=raw_input("\nEnter the Name: ")
		emp=input("\nEnter the Emp Number: ")
                ds=raw_input("\nEnter the Designation: ")
                sl=input("\nEnter the Salary: ")
                ph=raw_input("\nEnter the Phone Number: ")
		data2=np.array([(n,emp,ds,sl,ph)],dtype=dt1)
		data1=np.concatenate([data1,data2],axis=0)
	elif k=='c':
		eno=input("\nEnter employee number : \n ")
		i=np.where(data1==data1[data1['eno']==eno])
		data1=np.delete(data1,i)
	elif k=='d':
		inp=input("\nEnter employee number or name : \n")
 		if type(inp) is str:
			print data1[data1['ename']==inp]
		else:
			print data1[data1['eno']==inp]
	elif k=='e':
		te=len(data1)
		print "\nTotal Number of Employees : ",te
		print "\nTotal Employee Salary : ",data1['esalary'].sum()
	elif k=='f':
		np.savetxt('emp.csv',data1,fmt="%s,%d,%s,%f,%s")
	print data1
