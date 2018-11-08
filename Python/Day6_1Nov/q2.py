import sys as s
f=open(s.argv[1],'a')
m = [x*int(s.argv[2]) for x in range(1,11)]
res = str()
for i in range(1,11):
	res+= str(i)+"X"+str(s.argv[2])+"="+str(m[i-1])+"\n"
f.write(res)
f.close()
