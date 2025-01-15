# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 09:19:41 2024

@author: viren
"""
#23/9


import numpy as np
from numpy import array
from scipy.linalg import svd
A=array([[1,0,0,0,2],[0,0,3,0,0],[0,0,0,0,0],[0,4,0,0,0]])
print(A)
#SVD
U,d,Vt=svd(A)
print(U)
print(d)
print(Vt)
print(np.diag(d))
#SVD applying to a dataset
import pandas as pd
data=pd.read_csv("D:/data science/9-PCA & SVD/University_Clustering.csv",thousands=',')
data.head()
data=data.iloc[:,2:] #removes non numeric data
data
from sklearn.decomposition import TruncatedSVD
svd=TruncatedSVD(n_components=3)
svd.fit(data)
result=pd.DataFrame(svd.transform(data))
result.head()
result.columns="pc0","pc1","pc2"
result.head()
#Scatter diagram
import matplotlib.pylab as plt
plt.scatter(x=result.pc0, y=result.pc1,)
