import abc
class Employee:
	__metaClass__=abc.ABCMeta
	def __init__(self,nm,nn,nb):
		self.n=nm
		self.no=nn
		self.bp=nb
		self.da=nb*0.3
		self.hra=nb*0.1
		self.sp=0
	def disp(self):
		print "Name: %s,No: %d,Basic Pay: %d,DA: %d,HRA: %d,SPA: %d" % (self.n,self.no,self.bp,self.da,self.hra,self.sp)
	@abc.abstractmethod
	def Chra(self):
		pass
	def Csp(self):
		pass
class Engineer(Employee):
	def Csp(self):
		self.sp=self.bp*0.2
class Officer(Employee):
	def Csp(self):
		self.sp=self.bp*0.1
class JuniorEng(Engineer):
	def Chra(self):
		self.hra+=500
class SeniorEng(Engineer):
        def Chra(self):
                self.hra+=1000
A=Officer("Varun",111,10000)
B=JuniorEng("Shibin",122,15000)
C=SeniorEng("Tom",133,20000)
A.Csp()
B.Csp()
C.Csp()
B.Chra()
C.Chra()
A.disp()
B.disp()
C.disp()
	
