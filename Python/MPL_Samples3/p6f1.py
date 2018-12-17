#!/usr/bin/python
from pandas import Series as s
from pandas import DataFrame as f
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
fsales=f(np.random.randint(1,100,20).reshape(5,4))
fsales.columns='Jan Feb Mar Apr'.split()
fsales.index='V W X Y Z'.split()
so=fsales.plot(kind='bar')
#so.set_xticks([0,1,2,3,4])#not required
so.set_xticklabels('A B C D E'.split())#will work
print fsales
plt.show()
