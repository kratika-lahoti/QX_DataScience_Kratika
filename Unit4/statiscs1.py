# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 20:04:39 2019

@author: Kratika
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
df1 = pd.DataFrame(dict(id=range(6), age=np.random.randint(18, 31, size=6)))
print(df)