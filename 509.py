#numpy
import numpy as np
a = np.array([1,2,np.nan,4])
a = np.nan_to_num(a)
print(a)