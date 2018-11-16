
import re
def IsInteger(s):
	p=re.compile('?=[\d]')
	r=re.match(p,s)
	if r:
		return True
	return False
def IsFloat(s):
	p=re.compile('?=[\d+.\d+]')
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
def IsHex(s):
	p=re.compile('.*(?=[0-9,a-f]).*')
	r=re.match(p,s)
	if r:
		return True
	return False
def IsDate(s):
	p=re.compile('.*(?=[\d\d-\d\d-\d\d\d\d]).*')
        r=re.match(p,s)
        if r:
                return True
        return False
def IsValidPassword(s):
        p=re.compile('^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.{8,16})')
        r=re.match(p,s)
        if r:
                return True
        return False
def IsValidEmail(s):
        p=re.compile('^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$')
        r=re.match(p,s)
        if r:
                return True
        return False

st=raw_input("Enter the string: ")
print "Contains Intiger : ",IsInteger(st)
print "Contains Float : ",IsFloat(st)
print "Contains Vowels : ",HasVowel(st)
print "Contains Hex : ",IsHex(st)
print "Strong Password : ",IsValidPassword(st)
print "Valid Email : ",IsValidEmail(st)
