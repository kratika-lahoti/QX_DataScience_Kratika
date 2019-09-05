# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 18:27:48 2019

@author: Kratika
"""

import matplotlib.pyplot as plt
x=[1,2,3,4,5,6,7,8]
y=[5,2,4,2,1,4,5,2]

plt.scatter(x,y,label='sky',color='r',s=100 ,marker='o')
plt.xlabel('x')
plt.ylabel('y')
plt.title('scatter plot')
plt.legend()
plt.show()