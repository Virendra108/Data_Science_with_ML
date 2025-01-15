# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 08:58:01 2024

@author: viren
"""

import numpy as np
import matplotlib.pyplot as plt
#lets define a true value that we want to measure
#we first define the true value oof 50 This is the reference point
true_value=50

#Simulate data
#1.Accurate but not precise (close to true value and grouped tightly)_
'''
loc=true_value(True value=50):The values will be centered around the tru value(50)
scale=1 : The standard dev(spread) is small,
meaning the values will be tightly grouped around the true value.
This implies high precision .
The measurements will vary only a little from the true value.
so they'll be both accurate (close to 50) and precise(close to each other)
'''

accurate_precise=np.random.normal(loc=true_value,scale=1,size=10)
#2. Accurate but not precise (close to true value but spread out)
accurate_not_precise=np.random.normal(loc=true_value,scale=10,size=10)
'''
The two lines of code you've highlighted may look similar,
but they differ in one imp aspect : the value of scale,which controls the spread of the generated values around the true values (loc)
'''

#3.Precise but not Accurate (far from true value but tightly grouped)
precise_not_accurate=np.random.normal(loc=70,scale=1,size=10)


#4. Neither accurate not precise (far from true va;ue and spread out)
not_accurate_not_precise=np.random.normal(loc=70,scale=10,size=10)

#ploting the results
plt.figure(figsize=(10,6))

#Plot 1: Accurate and precise
plt.scatter(accurate_precise,[1]*10,color='green',label='Accurate and precise')

#Plot 2: Accurate but not precise
plt.scatter(accurate_not_precise,[2]*10,color='blue',label='Accurate but Not Precise')

#Plot 3: precise but not  accurate
plt.scatter(precise_not_accurate,[3]*10,color='orange', label='Precise but not Accurate')

#plot 4:Neither precise nor accurate
plt.scatter(not_accurate_not_precise,[4]*10,color='purple', label='Neither Accurate no Precise')

#Adding target line
plt.axvline(x=true_value, color='red', linestyle='--', label='True Value')

#labels and legend
plt.xlabel('Measurement')
plt.ylabel('Value')
plt.title('Accuracy and Precision')
plt.legend()
plt.show()