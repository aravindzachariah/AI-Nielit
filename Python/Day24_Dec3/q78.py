import pandas as pd
df=pd.read_csv("lsf3",header=None,skiprows=1)
df=df.sort_values(4,ascending=True)
print df
df.to_csv("lsf5",header=None)
