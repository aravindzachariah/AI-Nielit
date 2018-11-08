def div_f(**num):
	q=num['dv']/num['ds']
	r=num['dv']%num['ds']
	return q,r
try:
	a=input()
	b=input()
	r1,r2=div_f(dv=a,ds=b)
except:
	print "Cannot Divide By Zero "
else:
	print r1,r2
finally:
	print "Math operation Success"
