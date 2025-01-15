# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 08:33:52 2024

@author: viren
"""

#24/9

import pandas as pd
import numpy as np
Univ1=pd.read_csv("D:/data science/9-PCA & SVD/University_Clustering.csv",thousands=',')
Univ1.describe()
Univ1.info()
Univ=Univ1.drop(["State"],axis=1)
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale
Univ.data=Univ.iloc[:,1:]
#normalizing numerical data
uni_normal=scale(Univ.data)
uni_normal
pca=PCA(n_components=6)
pca_values=pca.fit_transform(uni_normal)
var=pca.explained_variance_ratio_
var
#PCA weights
pca.components_
pca.components_[0]
#to check the cumulative variance
var1=np.cumsum(np.round(var,decimals=4)*100)
var1
  