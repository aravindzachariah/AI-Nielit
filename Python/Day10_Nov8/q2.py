class comp:
	def __init__(self,px,py):
		self.x=px
		self.y=py
	def dispv(self):
		print "The complex number is (%2f+%2fi) " % (self.x,self.y)
	def __add__(self,pv1):
		xn=self.x+pv1.x
		yn=self.y+pv1.y
		return comp(xn,yn)
	def __equ__(self,pv2):
		if self.x==pv2.x and self.y==pv2.y:
			return True
		else:
			return False
c1=comp(1,2)
c2=comp(3,4)
c1.dispv()
c2.dispv()
c3=c1+c2
c3.dispv()
print "V1 = V2 ? : ",c1==c2

