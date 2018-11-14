import re
f1=open("emp.csv",)
f2=open("ini2.csv",'w')
for i in f1:
	mo=re.match('.*[A-Z]\\.',i)
	if mo:
		f2.write(i)
f2.close()		
