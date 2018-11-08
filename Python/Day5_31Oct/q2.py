def div_f(**num):
	q=num['dv']/num['ds']
	r=num['dv']%num['ds']
	return q,r
a=input()
b=input()
r1,r2=div_f(dv=a,ds=b)
print r1,r2
