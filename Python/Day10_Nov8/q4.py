class A:
	def __init__(self):
		print "This is me "
class B(A):
	def __init__(self):
		print "Talking to me in you "
class C(B):
	def __init__(self):
		print "Through me in me "
a=A()
b=B()
c=C()
