#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np
fobj=plt.figure(figsize=(14,8),facecolor='#00FF00')
spobj=fobj.add_subplot(1,1,1)
stud_name_xticks='Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'.split()
x_val=np.arange(len(stud_name_xticks))
rain_fall=[21,20,40,119,216,341,239,156,175,268,192,69]
spobj.stackplot(x_val,rain_fall)
spobj.set_xticks(x_val)
spobj.set_xticklabels(stud_name_xticks)
spobj.margins(0.1)
plt.show()
