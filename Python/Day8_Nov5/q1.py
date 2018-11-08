class Employee:
	def __init__(self):
		self.name=raw_input("Name : ")
		self.empno=raw_input("EmpNo : ")
		self.bp=raw_input("Basic Pay : ")
class Scientist(Employee):
	
	def __init__(self):
		Employee.__init__(self)
		self.ta=raw_input("TA : ")
		self.cat=raw_input(" Category :")
	def p1(self):
		print "\n\nName : ",self.name
		print "Emp No : ",self.empno
		print "Basic pay : ",self.bp
		print "TA : ",self.ta
		print "Category : ",self.cat 		
class Officer(Employee):
	def __init__(self):
		Employee.__init__(self)
		self.gd=raw_input("Grade : ")
		self.dpt=raw_input("Department : ")
	def p2(self):
		print "\n\nName : ",self.name
                print "Emp No : ",self.empno
                print "Basic pay : ",self.bp
                print "TA : ",self.gd
                print "Category : ",self.dpt   


S=Scientist()
O=Officer()
S.p1()
O.p2()
		
	
