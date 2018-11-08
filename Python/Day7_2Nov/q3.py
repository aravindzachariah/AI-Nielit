class BA:
	noa=0
	d=dict()
	def set(self):
		self.an=raw_input("Enter the account number : ")
		self.ab=0
		self.at=raw_input("Enter type : ")
		self.anm=raw_input("Enter the name : ")
		self.add=raw_input("Enter the address : ")
		BA.d[self.an]=[self.ab,self.at,self.anm,self.add]
		BA.noa=BA.noa+1
	def get(self,acno):
		print "Ac Balance :%d\nType : %s\nName : %s\nAddress: %s\n" % (BA.d[acno][0],BA.d[acno][1],BA.d[acno][2],BA.d[acno][3])
	def dep(self,acno):
		BA.d[acno][0]+=int(raw_input("Enter the deposit Amount : "))
	def wid(self,acno):
		BA.d[acno][0]=BA.d[acno][0]-int(raw_input("Enter the withdraw Amount : "))
B=BA()
c=0
while c<4:
	c=raw_input("\nEnter Choice\n1.Add acount\n2.Account Detail\n3.Deposit\n4.Withdraw\n5.Exit\n")
	c=int(c)
	if c==1:
		B.set()
	elif c==2:
		k=raw_input("Enter account no : ")
		B.get(k)
	elif c==3:
		k1=raw_input("Enter account no : ")
		B.dep(k1)
	elif c==4:
		k2=raw_input("Enter account no : ")
		B.wid(k2)


