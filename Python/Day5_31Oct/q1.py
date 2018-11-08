def div_f(dv,ds=2):
	q=dv/ds
	r=dv%ds
	return q,r
a=input()
b=input()
r1,r2=div_f(a,b)
print r1,r2
