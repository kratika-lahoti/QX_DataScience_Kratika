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
df1= pd.DataFrame({"Int_rate":[2,1,2,3,4],"Ind_GDP":[50,45,45,67,55]},
            index = [2001,2002,2003,2004,2222])
df2= pd.DataFrame({"low_Tier_HPI":[2,7,2,8,6],"unemployment":[50,45,45,67,44]},
            index = [2001,2003,2004,2004,6578])

joined= df1.join(df2)

print(joined)
 