import numpy as np
def dist(x1,y1,x2,y2):
   x=(x2-x1)**2
   y=(y2-y1)**2
   d=np.sqrt(x+y)
   print "The distance between points is",d

dist(1,2,3,4)
