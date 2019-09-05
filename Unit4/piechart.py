# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 21:36:04 2019

@author: Kratika
"""





import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

a= sns.load_dataset ("flight")
sns.relplot(x="passengers",y="month",data=a),hue="year"















