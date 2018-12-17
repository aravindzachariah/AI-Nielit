#!/usr/bin/python
from pandas import Series as s
from pandas import DataFrame as f
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
s1=s(range(1,6))
s1.index='one two three four five'.split()
so=s1.plot(kind='bar',rot=90)
#so.set_xticks(s1.index)
#so.set_xticklabels='one two three four five'.split()
print s1
plt.show()
