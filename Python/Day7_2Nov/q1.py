class Emp:
	def store(self):
		self.name=raw_input("Enter name : ")
		self.empno=raw_input("Enter number :")
		self.slry=raw_input("Enter the salary :")
	def disp(self):
		print "The employee name is : ",self.name
		print "The employee number is : ",self.empno
		print "The employee slalary is : ",self.slry
E=Emp()
E.store()
E.disp()
