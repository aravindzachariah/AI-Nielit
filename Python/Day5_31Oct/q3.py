print "Enter the options: "
print "1:Initialize"
print "2:Show"
print "3:Reload"
print "0:Exit"
while 1:
	k=input()
	if k==1:
		import q3mod 
		continue
	if k==2:
		print "con=",q3mod.a+(10*q3mod.b*q3mod.c)-5*q3mod.d/q3mod.e
		continue
	if k==3:
		reload(q3mod)
		continue
	else:
		break
 

