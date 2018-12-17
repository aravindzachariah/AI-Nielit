#!/usr/bin/python
from pandas import Series as s
from pandas import DataFrame as f
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
fsales=f(np.random.randint(1,100,20).reshape(5,4))
fsales.index='apple orange grapes mango banana'.split()
fsales.columns='Jan Feb Mar Apr'.split()
so=fsales.plot(kind='bar',rot=45)
print fsales
plt.show()
