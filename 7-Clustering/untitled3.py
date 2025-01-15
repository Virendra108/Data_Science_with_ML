# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 08:26:43 2024

@author: viren
"""

#9AUG 24

import pandas as pd
import matplotlib.pylab as plt
univ1=pd.read_excel("D:/data science/7-Clustering/University_Clustering.xlsx")
a=univ1.describe()
#we have one coluumn "state" whiich really not useful we will drop it
univ=univ1.drop(["State"],axis=1)
#we know that there is scale difference among the columns,
#which we have to remove
#either by using normaalization or standardization
#whenewver ther ismixed data apply normalizzation
def norm_func(i):
    x=(i-i.min())/(i.max()-i.min())
    return x
#now apply this normalization functionto univ datframe 
#for all the rows and columns from i until end
#since 0 th column has university name hence skippped
df_norm=norm_func(univ.iloc[:,1:])
#you can check the df_norm dataframe which is scaled
#between values of0 to 1
#you can aply describe() function to new dataframe
b=df_norm.describe()
'''Before you apply clustering you need to plot dendogram first
Now to create dendogram we need to measure distance
we have to import linkage'''
from scipy.cluster.hierarchy import linkage
import scipy.cluster.hierarchy as sch
#linkage function gives us hierarchical or aglomerative clustering
#ref the help for linkage
z=linkage(df_norm,method="complete",metric="euclidean")
plt.figure(figsize=(15,8))
plt.title("Hireraarchical clustering dendogram")
plt.xlabel("Index")
plt.ylabel("Distance")
#ref help of dendrogram
sch.dendrogram(z,leaf_rotation=0,leaf_font_size=10)
plt.show()
#applying aglomerative clustering choosing 5 as clusters from dendrogram
#whatever has been displayed in dens=drogrm is not clustering
#it is just showing number of possible clusters.
from sklearn.cluster import AgglomerativeClustering
h_complete=AgglomerativeClustering(n_clusters=3,linkage="complete",metric="euclidean").fit(df_norm)
#simply label to the clusters
h_complete.labels_
cluster_labels=pd.Series(h_complete.labels_)
#assign this series to Univ Dataframe as column and name the column
univ['clust']=cluster_labels
#we want to replace the column 7 to 0 th position
univ1=univ.iloc[:,[7,1,2,3,4,5,6]]
#now check the univ 1 datframe
univ1.iloc[:,2:].groupby(univ1.clust).mean()
#from the output cluster 2 has got highest top10
#store it to csv
