import re
f1=open("emp.csv",)
f2=open("emp2.csv",'w')
for i in f1:
	mo=re.split(',',i)
	me=re.match('[2-9][0-9][0-9]',mo[1])
	if me:
		f2.write(i)
f2.close()		
