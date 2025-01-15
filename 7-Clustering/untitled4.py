# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 08:58:23 2024

@author: viren
"""

# Importing necessary libraries
from sklearn.cluster import KMeans
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from matplotlib import pyplot as plt

# Reading the dataset
df = pd.read_csv("income.csv")

# Displaying the first few rows of the dataset
df.head()

# Plotting a scatter plot of Age vs. Income
plt.scatter(df.Age, df['Income($)'])
plt.xlabel('Age')
plt.ylabel('Income($)')
plt.show()

# Creating a KMeans model with 3 clusters
km = KMeans(n_clusters=3)

# Fitting the model and predicting the clusters
y_predicted = km.fit_predict(df[['Age', 'Income($)']])

# Adding the cluster predictions to the dataframe
df['cluster'] = y_predicted

# Displaying the first few rows with the cluster information
df.head()

# Displaying the cluster centers
km.cluster_centers_

# Creating dataframes for each cluster
df1 = df[df.cluster == 0]
df2 = df[df.cluster == 1]
df3 = df[df.cluster == 2]

# Plotting the clusters with different colors
plt.scatter(df1.Age, df1['Income($)'], color='green', label='Cluster 1')
plt.scatter(df2.Age, df2['Income($)'], color='red', label='Cluster 2')
plt.scatter(df3.Age, df3['Income($)'], color='black', label='Cluster 3')

# Plotting the cluster centers
plt.scatter(km.cluster_centers_[:, 0], km.cluster_centers_[:, 1], color='purple', marker='*', label='Centroid')

# Adding labels and legend
plt.xlabel('Age')
plt.ylabel('Income($)')
plt.legend()
plt.show()

#preprocessing using min max scaling
scaler=MinMaxScaler()
scaler.fit(df[['Income($)']])
df['Income($)']=scaler.transform(df[['Income($)']])
scaler.fit(df[['Age']])
df['Age']=scaler.transform(df[['Age']])
df.head()
plt.scatter(df.Age,df['Income($)'])

km=KMeans(n_clusters=3)
y_predicted=km.fit_predict(df[['Age','Income($)']])
y_predicted

df['cluster']=y_predicted
df.head()
km.cluster_centers_

# Creating dataframes for each cluster
df1 = df[df.cluster == 0]
df2 = df[df.cluster == 1]
df3 = df[df.cluster == 2]

# Plotting the clusters with different colors
plt.scatter(df1.Age, df1['Income($)'], color='green', label='Cluster 1')
plt.scatter(df2.Age, df2['Income($)'], color='red', label='Cluster 2')
plt.scatter(df3.Age, df3['Income($)'], color='black', label='Cluster 3')
# Plotting the cluster centers
plt.scatter(km.cluster_centers_[:, 0], km.cluster_centers_[:, 1], color='purple', marker='*', label='Centroid')
# Plotting the cluster centers
plt.scatter(km.cluster_centers_[:, 0], km.cluster_centers_[:, 1], color='purple', marker='*', label='Centroid')
