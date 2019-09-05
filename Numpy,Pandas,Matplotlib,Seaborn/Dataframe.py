# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 21:36:04 2019

@author: Kratika
"""



 import matplotlib.pyplot as plt
 
 slices = [7,2,2,13]
 activies=['sleeping','eating','working','playing']
 cols=['c','m','r','b']
 
 plt.pie(slices,
         labels=activities,
         colors=cols,
         shadow=True,
         explode=(0,0.1,0,0),
         autopct='%1.1f%%')
 plt.title('pie plot')
 plt.show()
         
         
         
         
         
         
         
         
         )