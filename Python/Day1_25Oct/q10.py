def dist(x1,y1,x2,y2):
	x=(x2-x1)**2
	y=(y2-y1)**2
	d=(x+y)**0.5
        return d	
print "Enter the coordinates of First point"
x1=input()
y1=input()
print "Enter the coordinates of Second point"
x2=input()
y2=input()
d=dist(x1,y1,x2,y2)
print "The distance between points is",d


