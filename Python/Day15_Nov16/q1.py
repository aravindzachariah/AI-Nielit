import re
def isInteger(s):
	p=re.compile('(?=[0-9])')
	r=re.match(p,s)
	if r:
		return True
	return False
def isFloat(s):
	p=re.compile('(?=\d)')
	r=re.match(p,s)
	if r:
		return True
	return False
def HasVowel(s):
	p=re.compile('.*(?=[aeiouAEIOU]).*')
	r=re.match(p,s)
	if r:
		return True
	return False
def isHex(s):
	p=re.compile('(?=\\x)')
	r=re.match(p,s)
	if r:
		return True
	return False
st=raw_input("Enter the string: ")
print "Contains Intiger : ",isInteger(st)
print "Contains Float : ",isFloat(st)
print "Contains Vowels : ",HasVowel(st)
print "Contains Hex : ",isHex(st)
