import numpy as np
print "Enter the coordinates of First point"
x1=input()
y1=input()
print "Enter the coordinates of Second point"
x2=input()
y2=input()
x=(x2-x1)**2
y=(y2-y1)**2
d=np.sqrt(x+y)
print "The distance between points is",d

