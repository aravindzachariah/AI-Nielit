#!/usr/bin/python
from pandas import Series as s
from pandas import DataFrame as f
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
s1=s([.3,.22,.2])
s1.name='Halfs'
s1.index='one two three'.split()
so=s1.plot(kind='pie',autopct='%22.2f')
print s1
plt.show()
