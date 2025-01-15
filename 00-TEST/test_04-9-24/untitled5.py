# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 09:20:10 2024

@author: viren
"""

import numpy as np
'''1. Given a dataset of integers or floating-point numbers, calculate the
following descriptive statistics:
 Mean
 Median
 Mode
 Variance
 Standard Deviation
Sample Dataset: [20, 40, 40, 40, 30, 50, 60]
'''

set1=[20, 40, 40, 40, 30, 50, 60]
m1=np.mean(set1)
med=np.median(set1)
mod=np.mode(set1)
var=np.var(set1)
sd=np.std(set1)

print(f"mean:{m1}, median:{med},  variance:{var},  standarddeviation:{sd}")



'''2. Generate a dataset of 1,000 random values generated from a lognormal
distribution with a mean of 0 and a standard deviation of 1 in the log-space,
perform the following tasks:
 Plot the histogram of the dataset.
 Calculate the mean and median of the dataset.
 Fit a lognormal distribution to the data and overlay the probability density
function (PDF) on the histogram.
'''
import matplotlib.pyplot as plt
from scipy.stats import lognorm
data = np.random.lognormal(mean=0, sigma=1, size=1000)
mean_val= np.mean(data)
median_val= np.median(data)





'''3. Generate 1,000 random values following a logarithmic distribution with
a probability parameter p = 0.3. Perform the following tasks:
 Plot the histogram of the dataset.
 Calculate the mean of the dataset.
 Overlay the probability mass function (PMF) of the logarithmic
distribution on the histogram.
'''








'''4. Given a dataset containing various types of data, categorize each
variable into the appropriate statistical data type: Nominal, Ordinal,
Interval, or Ratio. Then, write code to demonstrate how you would work
with each type of data.
Example Dataset:
ID Name Age Education
Level
Salary Joining
Year
1 Sophie 22 Bachelor's 60000 2022
2 Aryan 25 Master's 75000 2020
3 Amit 28 PhD 78000 2018
4 Charu 26 Bachelor's 45000 2015
5 Piyush 37 Master's 92000 2010

'''





'''5. Given a data of house prices [200000, 250000, 150000, 350000, 300000,
400000, 450000, 600000, 650000, 500000, 550000]. Calculate the following:
 The median of the dataset.
 The 25th percentile (1st quantile), 50th percentile (2nd quantile, also the
median), and 75th percentile (3rd quantile).
 Visualize the data using a box plot.
'''

import numpy as np
import matplotlib.pyplot as plt

# House prices dataset
prices = [200000, 250000, 150000, 350000, 300000,
          400000, 450000, 600000, 650000, 500000, 550000]

# Calculate median
hmed = np.median(prices)
print(f"Median (50th percentile): {hmed}")

# Calculate percentiles
per25 = np.percentile(prices, 25)
per50 = np.percentile(prices, 50)
per75 = np.percentile(prices, 75)

print(f"25th percentile: {per25}")
print(f"50th percentile: {per50}")
print(f"75th percentile: {per75}")

# Create box plot
plt.figure(figsize=(10, 6))
plt.boxplot(prices, vert=False, patch_artist=True, 
            boxprops=dict(facecolor='blue', color='blue'),
            whiskerprops=dict(color='blue'),
            capprops=dict(color='blue'),
            medianprops=dict(color='red'))
plt.xlabel('House Price')
plt.title('Box Plot of House Prices')
plt.show()

