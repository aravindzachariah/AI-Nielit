import pandas as pd
from pandas import DataFrame as f
import numpy as np
df=f(np.random.randint(10,20,40).reshape(10,4),columns="c1 c2 c3 c4".split())
print df 
print df.sort_values(['c1','c3'],ascending=[True,False])
