# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 09:07:00 2024

@author: viren
"""

import numpy as np
#lets defie true value that we want to measure
#we first define the true value of 50. this is the refernece point
true_value=50

#simuate some measurements
#Accurate but not precuse (close to true value but spread oout)

'''we simulate two setsd of measurement:
    value(50) but ther eis some spread (random varaition)
    This simulates measurements that are accuaretee
    (close to true value ) but not precise (spread out).
'''

accuarete_measurements=np.random.normal(loc=true_value,scale=5,size=10)


#precise but not accurate

'''
precise but not accurate:
    thes values are tightly clustred around 60,
    not nera the vs=true vslue of 50.
    This simulayes measuremetns that are precise (closely grouped)
    but not accurate(far from true value)
'''

precise_measurements=np.random.normal(loc=60,scale=1,size=10)

#Function to calculate accuracy
'''
we calculate the mean (average) of the measurements
Then we calculate oow clos this average is to true value.
The closer the average  is to true value,
higher thea scciuracy,.

accuaracy formaula is 1-(difference/true_value)
This give a number between 0(loa accur) and 1 (high accur).
'''

def calculate_accuracy(measurements, true_value):
    average_measurement=np.mean(measurements)
    accuracy=1-abs(average_measurement-true_value)/true_value
    return accuracy

'''
Precision is determined by the standard deviation
of the measurements.Standard deviation measures how the spread out the measurements are.
if the standard deviation is small
(measurements are close together),
precision will be high.We use 1/std_dev to represent precision,
to a smaller spread gives a higher value for precision.
'''


def calculate_precision(measurements):
    #precision how close the measuemtns are to each other
    #low SD means hihg precsiion
    precision=1/np.std(measurements)
    #means lower precision s o wew invert it
    return precision


'''
Accurate measurements:we calculate the accuracy and precision
of the measurements that are close to the true value but spread out,
Precise measurements:we calculate the accuracy and precision
of the measurments that are closely grouped but from the true value.'''


accuaracy_of_accurate=calculate_accuracy(accuarete_measurements, true_value)
precision_of_accurate=calculate_precision(accuarete_measurements)

accuaracy_of_precise=calculate_accuracy(precise_measurements, true_value)
Precision_of_precise=calculate_precision(precise_measurements)


#print hte results
print(f"Accurate but not precise Measurements:")
print(f"Measurements: {accuarete_measurements}")
print(f"Accuracy: {accuaracy_of_accurate:.2f}")
print(f"precision: {precision_of_accurate:.2f}")



print(f"\nAccurate but not precise Measurements:")
print(f"Measurements: {precise_measurements}")
print(f"Accuracy: {accuaracy_of_precise:.2f}")
print(f"precision: {Precision_of_precise:.2f}")