# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 13:28:21 2019

@author: Kratika
"""

a=sns.load_dataset("iris")
b=sns.Facetgrid(a, col="species")
b.map(plt.hist,"sepal_length")