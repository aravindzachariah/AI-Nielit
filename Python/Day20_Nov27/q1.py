import numpy as np
import pandas as pd
dt1=np.dtype([('ename','S20'),('eno','i8'),('edesign','i8'),('esalary','f8'),('ephno','S15')])
alf=np.loadtxt('emp.csv',delimiter=",",dtype=dt1)
print alf
