class vect:
	def __init__(self,px,py):
		self.x=px
		self.y=py
	def dispv(self):
		print "The vector is (%2f,%2f) " % (self.x,self.y)
	def __add__(self,pv1):
		xn=self.x+pv1.x
		yn=self.y+pv1.y
		return vect(xn,yn)
v1=vect(1,2)
v2=vect(3,4)
v1.dispv()
v2.dispv()
v3=v1+v2
v3.dispv()

