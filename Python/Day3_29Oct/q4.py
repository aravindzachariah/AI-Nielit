s=raw_input()
k=0
v="aeiou"
for i in s:
	if i in v:
		k+=1
if k>=2:
	print "True"
else:
	print "False"
