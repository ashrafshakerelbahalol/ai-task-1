# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 17:42:51 2021

@author: ZOZ
"""

import pandas as pd
import matplotlib.pyplot as plt
dataset=pd.read_csv("Wuzzuf_Jobs.csv")
dataset.describe()
print(dataset)
dataset.drop_duplicates( inplace = True)
dataset.dropna( inplace = True)
x=dataset['Company'].value_counts()
print(dataset.head(1))
plt.pie(x)
plt.show() 

t=dataset['Title'].value_counts()
dataset.sort_values("Title", inplace = True)
print(dataset.head(1))
plt.barh(t.index,t,height = 0.5, color='green', edgecolor="black", linewidth=0.1);
plt.show()

q=dataset['Location'].value_counts()
dataset.sort_values("Location", inplace = True)
print(dataset.head(1))
plt.barh(q.index,q,height = 0.5, color='green', edgecolor="black", linewidth=0.1);
plt.show()