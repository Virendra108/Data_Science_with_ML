# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 08:39:40 2024

@author: viren
"""
#eda
#data pre-processing

import pandas as pd
df=pd.read_csv("D:/data science/5-Data_prep/ethnic diversity.csv")
df.dtypes
#salaroes data tyep is float let us convert into int
#df1=df.Salaries.astype(int)
df.Salaries=df.Salaries.astype(int)
df.dtypes
#noe the data type of salries is int similarly age type mus be float presentlty
#it is int
df.age=df.age.astype(float)
df.dtypes


############################################               
df_new=pd.read_csv("D:/data science/5-Data_prep/education.csv")
duplicate=df_new.duplicated()
#output of this function is single column if there is duplicate then TRUE 
#if no duplicate then False
#Series will be created
duplicate
sum(duplicate)
#out[ut is 0]
#now let us import ansother data set
df_new1=pd.read_csv("D:/data science/5-Data_prep/mtcars_dup.csv")
duplicate1=df_new1.duplicated()
duplicate1
sum(duplicate1)
#there are 3 duplicate values
#row 17 is duplicate of row2 like wise you can see 3 dupolciates
#there is function called drop_duplicatee()
#which will drop all duplicate records
df_new2=df_new1.drop_duplicates()
duplicate2=df_new2.duplicated()
duplicate2
sum(duplicate2)

########################################
import pandas as pd
import seaborn as sns
df=pd.read_csv("D:/data science/5-Data_prep/ethnic diversity.csv")
#now let us find outliers in salaries
sns.boxplot(df.Salaries)
#there are ouliers
#let us check outliers in age column
sns.boxplot(df.age)
#there are no utliers let us calculate iqr
IQR=df.Salaries.quantile(0.75)-df.Salaries.quantile(0.25)
#have observed IQR in variable explorer
#no because IQR is in capital letters
#treated as constanrt
IQR
#but if we wil try as I,Iqr or iqr then it is showing
iqr=df.Salaries.quantile(0.75)-df.Salaries.quantile(0.25)
iqr
IQR
'''1/8/24'''


lower_limit=df.Salaries.quantile(0.25)-1.5*IQR
upper_limit=df.Salaries.quantile(0.75)+1.5*IQR
#now if you willl check lower limit of salarie it is -19446.9675
#upper limit is 93992.8125
#there is negative salary so   make it 0
#go to variable exploere and make it zero
#######################################################
#Trimming
import numpy as np
outliers_df=np.where(df.Salaries>upper_limit,True,
                     np.where(df.Salaries<lower_limit,True,False))
#you can check outliers of column in variable explorer
df_trimmed=df.loc[~outliers_df]
df.shape
#(310,13)
df_trimmed.shape
#(306,13)
sns.boxplot(df_trimmed.Salaries)
########################################################
df=pd.read_csv("D:/data science/5-Data_prep/ethnic diversity.csv")
df.describe()
#recorrd no 23 has got outliers
#map all the outliar values to upper limit
df_replaced=pd.DataFrame(np.where(df.Salaries>upper_limit,upper_limit,np.where(df.Salaries<lower_limit,lower_limit,df.Salaries)))
#if  the values are greater than upper_limit map it to upper limit
#and less than lower_limit map it to lower limit, if it is within the range
#then keep as it is
sns.boxplot(df_replaced[0])
#######################################################
#winsorizer
from feature_engine.outliers import Winsorizer
winsor=Winsorizer(capping_method='iqr',tail='both',fold=1.5,variables=['Salaries'])
#copy Winsorizer ad paste in help tab of top right window, study the method
df_t=winsor.fit_transform(df[['Salaries']])
sns.boxplot(df['Salaries'])
sns.boxplot(df_t['Salaries'])
####################################################
'''2-8'''
#zero variance and near zero variance
#if there is no variance in feature then ML will not got any inteelligence

import pandas as pd
df=pd.read_csv("D:/data science/5-Data_prep/ethnic diversity.csv")
df.var()
#here EmpID and ZIP is nominal data
#salarry has 4.441953e+08 is 4441953000 which is not clos to 0
#similar for age also
#bith the features having considerable variance
df.info()
df.Salaries.var()==0
'''
EMP ID      False
ZIP         False
Salaries    False
age         False
'''
df.var(axis=0)==0
#error, sohave to check column wise

import numpy as np
df=pd.read_csv("D:/data science/5-Data_prep/modified ethnic.csv")
#check for null values
df.isna().sum()
'''
Position            43
State               35
Sex                 34
MaritalDesc         29
CitizenDesc         27
EmploymentStatus    32
Department          18
Salaries            32
age                 35
Race                25
'''
#create an inmpute that creates nullvvalues
#mean and median is used for numeric data
#mode is ud=sed for discrete data(position,sex,MaritalDes)
from sklearn.impute import SimpleImputer
mean_imputer=SimpleImputer(missing_values=np.nan,strategy='mean')
#check the dataframe
df['Salaries']=pd.DataFrame(mean_imputer.fit_transform(df[['Salaries']]))
#check the dataframe
df['Salaries'].isna().sum()
#0
#meadian imputer
median_imputer=SimpleImputer(missing_values=np.nan,strategy='median')
df['Salaries']=pd.DataFrame(median_imputer.fit_transform(df[['Salaries']]))
df['Salaries'].isna().sum()
#0
#mode imputer
mode_imputer=SimpleImputer(missing_values=np.nan,strategy='most_frequent')
df['Salaries']=pd.DataFrame(mode_imputer.fit_transform(df[['Salaries']]))
df['Salaries'].isna().sum()
#0

df['MaritalDesc']=pd.DataFrame(mode_imputer.fit_transform(df[['MaritalDesc']]))
df['MaritalDesc'].isna().sum()
#0

##############################################################
#pip install imbalanced-learn scikit-learn
import numpy as np
from sklearn.datasets import make_classification
from imblearn.over_sampling import SMOTE
'''IMP INTERVIEW QUESTION:
#to treate your imbalanced data you will use smote technique'''
#step1: Generate an imbalanced dataset
X, y=make_classification(n_samples=1000, n_features=20, n_informative=2, n_redundant=10, n_clusters_per_class=1, weights=[0.99], flip_y=0, random_state=1)


'''
parametres
n_samples=1000:
            Thet total nummber of samples (data points) to generate.
            here 1000 sample will be created
            
n_features=20:
            total number of features(columsn) in the datase. here it is 20.
            
n_informative=2:
            total nunber of informatie fetures.
            these fetures are use ful for predicting thr target variable
            
n_redundant=10:
            these features are genrated as random linear combinations of the
            
cluster_per_class=1:
            number of cluster pweer class
            here 99% of sample belong to one class
            creating a significant class imbalance
            
            
            
'''

#show original class distribution
print("Original class distribution:",np.bincount(y))

#step2: Apply SMOTE to balace the dataset
smote= SMOTE(random_state=42)
X_res, y_res= smote.fit_resample(X, y)

#show the new class distributuion after appliying smote
print("Resample class distribution: ",np.bincount(y_res))

'''5/8/24'''

#show the original class distribution

print(f'Original_class distribution: {np.bincount(y)}')

#step2: Apply SMOTE to balance the dataset
smote=SMOTE(random_state=42)
X_res, y_res=smote.fit_resample(X, y)

#show the new class distrinbution after applying smote
print("Resample class distribution: ",np.bincount(y_res))

#show the original class distribution
print(f'Original class distribbutiion: {np.bincount(y)}')
from sklearn.model_selection import train_test_split
#step2: split the data into training and testing parts
X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.3,random_state=42)

#step3:Applty SMOTE to balance the training dataset
smote=SMOTE(random_state=42)
X_train_res, y_train_res=smote.fit_resample(X_train, y_train)

#show the class distribution after applying SMOTE
print(f'Resample class distrrinution: {np.bincount(y_train_res)}')

from sklearn.ensemble import RandomForestClassifier
#step4: Train classification on the balanced dataste
clf= RandomForestClassifier(random_state=42)
clf.fit(X_train_res, y_train_res)

#Step5: Evaluate classifier on the test set
y_pred=clf.predict(X_test)

from sklearn.metrics import confusion_matrix
print("Conclusion matrix:")
print(confusion_matrix(y_test,y_pred))





import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#generate sample dataset
np.random.seed(0)
data=np.random.exponential(scale=2.0, size=1000)
df=pd.DataFrame(data, columns=['Value'])

#perform log Transformation
df['logValue']=np.log(df['Value'])

#plot the original and log_transformed data
fig, axes = plt.subplots(1,2, figsize=(12,6))

