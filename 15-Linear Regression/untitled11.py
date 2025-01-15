# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 08:22:36 2025

@author: viren
"""
#multiple coreation regression analysis
import pandas as pd
import numpy as np
cars=pd.read_csv("D:/data science/15-Linear Regression/Cars.csv")


cars.describe()

import matplotlib.pyplot as plt
plt.bar(height=cars.HP,x=np.arange(1,82,1))
plt.hist(cars.HP)
plt.boxplot(cars.HP)
# There are several outliers inHP column
#similar operations are expected for other three column
# now let us plot joint plot Joint plot is to show scatter plot
#hISTOGRAM

import seaborn as sns
sns.jointplot(x=cars['HP'],y=cars['MPG'])

#Now let us plot count plot
plt.figure(1,figsize=(16,10))
sns.countplot(cars['HP'])
# Count plot shows how many times the each value occured
#92 HP value occured 7 times


##QQ plot
from scipy import stats 
import pylab
stats.probplot(cars.MPG,dist="norm",plot=pylab)
# MPG data is normally distributed
# There are 10 scatter plot need to be plotted , one by one
# in sequence to plot, so we can use pair plots

import seaborn as sns
sns.pairplot(cars.iloc[:,:])
#you can check the collinearity problem between the input variable
#you can check plot between SP and HP they are strongly corelated
#
#same way WT and VOL it is also hif=ghly corelated

#now let us check r value between variables
cars.corr()
#you can check SP and HP
#You can chech WT and VOL
#same way WT and VOl it has =got 0.99 which is greater

#now although we observe strongly correlated pairs still we will go for linear regression'
import statsmodels.formula.api as smf
ml1=smf.ols('MPG~WT+VOL+SP+HP',data=cars).fit()
ml1.summary()
#square value observation is



import statsmodels.api as sm
sm.graphics.influence_plot(ml1)
#76 is thevalue which has got outliers
#go to dataframe and check 76th entry
#let us delete that entry
cars_new=cars.drop(cars.index[[76]])

#again apply regression to cars_new
ml_new=smf.ols('MPG~WT+VOL+SP+HP',data=cars_new).fit()
ml_new.summary()

#r-square value is 0.819 but p values are same
#hence not solving the purpose
#Now next option is delete the column but question is which option is to be deleted
#w have already checked correlation factor r
#VOL has got -0.529 and for WT=-0.526
#WT is less hence can be deleted

#another appearance is to check 

rsq_hp=smf.ols('MPG~WT+VOL+SP',data=cars).fit().rsquared
vif_hp=1/(1-rsq_hp)
#VIF is variance influential factor calculating VIF helps to
#of x1 w.r.t x2,x3 and x4

rsq_wt=smf.ols('MPG~HP+VOL+SP',data=cars).fit().rsquared
vif_wt=1/(1-rsq_wt)

rsq_vol=smf.ols('MPG~HP+WT+SP',data=cars).fit().rsquared
vif_vol=1/(1-rsq_vol)

rsq_sp=smf.ols('MPG~HP+WT+VOL',data=cars).fit().rsquared
vif_sp=1/(1-rsq_sp)
#vif_WT=639.53 and vif_vol=638.80 hence vif_wt is greater, thus
#rule is vif should be greater then 10

#vif_wt=639.53,vif_vol=638.80 hence vif_wt is grater,thumb rule is vif sholud not be greater than 10

#storing the values in dataframe
d1={'Variables':['HP','WT','VOL','SP'],'VIF':[vif_hp,vif_wt,vif_vol,vif_sp]}
vif_frame=pd.DataFrame(d1)
vif_frame

#let us drop WT and apply correlation to remaining three
final_ml=smf.ols('MPG~VOL+SP+HP',data=cars).fit()
final_ml.summary()
#R square is 0.770 and p values 0.00,0.012<0.05

#prediction
pred=final_ml.predict(cars)

#QQ plot
res=final_ml.resid
sm.qqplot(res)
plt.show()
#This qq plot is on residual which os obtained on training data
#errors are obtained on test data
stats.probplot(res,dist='norm',plot=pylab)
plt.show()

#let us plot the residual plot which takes the residual values and the data
sns.residplot(x=pred,y=cars.MPG,lowess=True)
plt.xlabel
#QQ plot
res=final_ml.resid
sm.qqplot(res)
plt.show()
#this QQ plot is on residual which is obtained on training data
#erros are obtained on test data
stats.probplot(res, dist='norm', plot=pylab)
plt.show()

#let us plot the residual plot, which takes the residuals as values
#and the data
sns.residplot(x=pred, y=cars.MPG, lowess=True)
plt.xlabel('Fitted')
plt.ylabel('Residual')
plt.title('Fitted vs Residual')
plt.show()

sm.graphics.influence_plot(final_ml)

#plotting the data into train and test split
from sklearn.model_selection import train_test_split
cars_train,cars_test=train_test_split(cars,test_size=0.2)

model_train=smf.ols('MPG~VOL+SP+HP',data=cars_train).fit()
model_train.summary()
test_pred=model_train.predict(cars_test)

test_error=test_pred-cars_test.MPG
test_rese=np.sqrt(np.mean(test_error*test_error))
test_rese
