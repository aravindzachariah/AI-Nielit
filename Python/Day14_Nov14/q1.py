import re
f1=open("emp.csv")
f2=open("sci.csv",'w')
for i in f1:
	mo=re.match('.*scientist+.*',i)
	if mo:
		f2.write(i)
f2.close()		
