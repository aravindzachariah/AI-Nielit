f=open("f",'w')
n2=input("Enter the number : ")
m = [x*n2 for x in range(1,11)]
res = str()
for i in range(1,11):
	res+= str(i)+"X"+str(n2)+"="+str(m[i-1])+"\n"
f.write(res)
f.close()
