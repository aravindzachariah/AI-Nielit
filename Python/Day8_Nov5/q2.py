class Employee:
	def __init__(self):
		self.name=raw_input("Name : ")
		self.empno=input("EmpNo : ")
		self.bp=input("Basic Pay : ")
class Scientist(Employee):
	
	def __init__(self):
		Employee.__init__(self)
		self.ta=input("TA : ")
		self.cat=raw_input("Category :")
	def __str__(self):
		return " \nScientist %s with Emp No %d has a salary of %d and of Category %s and TA is %d" % (self.name,self.empno,self.bp,self.cat,self.ta)
	def p1(self):
		print "\n\nName : ",self.name
		print "Emp No : ",self.empno
		print "Basic pay : ",self.bp
		print "TA : ",self.ta
		print "Category : ",self.cat 		
class Officer(Employee):
	def __init__(self):
		Employee.__init__(self)
		self.gd=input("Grade : ")
		self.dpt=raw_input("Department : ")
	def __str__(self):
                return " Officer %s with Emp No %d has a salary of %d and of Department %s and Grade is %d" % (self.name,self.empno,self.bp,self.dpt,self.gd)
	def p2(self):
		print "\n\nName : ",self.name
                print "Emp No : ",self.empno
                print "Basic pay : ",self.bp
                print "Grade : ",self.gd
                print "Department : ",self.dpt   


S=Scientist()
O=Officer()
S.p1()
O.p2()
print str(S)
print str(O)		
	
