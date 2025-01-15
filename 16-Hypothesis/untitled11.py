# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 08:14:44 2025

@author: viren
"""
import pandas as pd
#Two sample T-Test
offers=pd.read_excel("D:/data science/16-Hypothesis/Promotion.xlsx")
offers.columns=["InterestRateWavier","StandardPromotion"]

#Normality Test
print("InterestRateWavier Normality:", stats.shapiro(offers.InterestRateWavier,offers.StandardPromotion))
print("StandardPromotion Normality:", stats.shapiro(offers.StandardPromotion))

#Variance Test
leven_test=scipy.stats.levene(offers.InterestRateWavier,offers.StandardPromotion)
print("Leven Test(Variance):",leven_test)

#pvalue=0.2875
#H0=variance equal
#H1=variance unequal
#pvalue=0.2875> 0.05 Fail to reject null hypothesis (H0 is accepted)
#Two- sample T-test
ttest_result=scipy.stats.ttest_ind(offers.InterestRateWavier, offers.StandardPromotion)
print("Two-sample T-Test: ", ttest_result)
#Result: p-value = 0.0242
#Interpretation:
#H0: Both offers have the same mean impact.
#H1: the mean impact of the two offer are different
#since the p value is less than 0.5, we reject null hyypothesis
#conclusion: There is a sinifcanar difference between the two promotionaal offers


#Mood's Median Test
#objective: Is the medians of pooh, piglet, and Tiger are statistically equal.
#it has equal medians or not

animals=pd.read_csv("D:/data science/16-Hypothesis/animals.csv")

#Normality Test
print("pooh Normality:",stats.shapiro(animals.Pooh))
#pvalue=0.0122
print("piglet Normality:",stats.shapiro(animals.Piglet))
#pvalue=0.044
print("Tigger Normality:",stats.shapiro(animals.Tigger))
#pvalue=0.0219
#H0: data is normal
#H1: data is not normal
#since all p values are less than 0.05 hence reject the null hypothesis
#data is not normal, hence Moods Test
#Median Test
median_test_result=stats.median_test(animals.Pooh, animals.Piglet, animals.Tigger)
print("Moods Median Test:",median_test_result)
#Result : p-value = 0.186
#Interpretation:
#H0: All groups have equal medians.
#H1: At least  one group has a diffeerent median.
#Conclusion: The medians of pooh, Piglet, and Tigger are statistically equal.

#one-way ANOVA
#objective: is the transaction times for the three suppliers are not
#significantly different
contract= pd.read_excel("D:/data science/16-Hypothesis/ContractRenewal_Data(unstacked).xlsx")
contract.columns=["Supp_A","Supp_B","Supp_C"]

#Normality test
print("Supp_A Normality:", stats.shapiro(contract.Supp_A))
print("Supp_B Normality:", stats.shapiro(contract.Supp_B))
print("Supp_C Normality:", stats.shapiro(contract.Supp_C))
#All p values are greater than 0.05
#we fail to reject the null hypothesis
#i.e. H0 is accepted means the data is normal
#Variance test
levene_test=scipy.stats.levene(contract.Supp_A, contract.Supp_B, contract.Supp_C)
print("Levenge Test (Variance):", levenge_test)
#H0: data is having equal variance
#H1: data is having ddifference in variance
#pvalue=0.7775>0.05 , H0 is accepted
#ANOVA TEst
anova_result=stats.f_oneway(contract.Supp_A, contract.Supp_B, contract.Supp_C)
print()