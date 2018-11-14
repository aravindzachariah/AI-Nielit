import re
f1=open("emp.csv",)
f2=open("empphno.csv",'w')
for i in f1:
	#mo=re.match('[^,]+',i)
	me=re.split((','),i)
	if me:
		name=me[0]
		no=me[-1]
		no=re.sub('[^0-9]+','',no)
		f2.write("%s,%s\n" % (name,no))
f2.close()		
