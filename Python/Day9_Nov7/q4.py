import abc
class vehcle:
	__metaclass__=abc.ABCMeta
	def __init__(self,pOwn,pNo,pW,pV,pY):
		self.nOwn=pOwn
		self.nNo=pNo
		self.nW=pW
		self.nV=pV
		self.nY=pY
		self.nP=0
	def disp(self):
		print "Vehicle Owner %s with No %s ,%d wheeler has value of Rs %d,YOM: %d " % (self.nOwn,self.nNo,self.nW,self.nV,self.nY)
	@abc.abstractmethod
	def calc(self):
		pass
class car(vehcle):
	def calc(self):
		self.nP=self.nV-(5000*(2018-self.nY))	
		print "Current Price : Rs",self.nP
class bus(vehcle):
        def calc(self):
                self.nP=self.nV-(1000*(2018-self.nY))   
                print "Current Price : Rs",self.nP
class truck(vehcle):
        def calc(self):
                self.nP=self.nV-(12000*(2018-self.nY))   
                print "Current Price : Rs",self.nP
C1=car("Aravind","KL-12-1224",4,200000,2008)
C1.disp()
C1.calc()
B1=bus("Aravind","KL-11-8115",4,2000000,2000)
B1.disp()
B1.calc()
T1=truck("Aravind","KL-13-7474",4,2000000,2006)
T1.disp()
T1.calc()

