# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 21:05:45 2019

@author: Kratika
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#kratika matplotlib program
import pandas as pd
df1= pd.DataFrame({"HPI":[80,90,70,60,10],"Int_rate":[2,1,2,3,4],"Ind_GDP":[50,45,45,67,55]},index = [2001,2002,2003,2004,2222])
df2= pd.DataFrame({"HPI":[80,90,70,60, 77],"Int_rate":[2,7,2,8,6],"Ind_GDP":[50,45,45,67,44]},index = [2005,2006,2007,2008,2223])
merge = pd.merge(df1,df2 ,how='outer',on="HPI",suffixes=('_krati','_piyu'),indicator=True)
print(merge)
 