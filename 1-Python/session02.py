# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 08:26:26 2024

@author: viren
"""


'''                             25/3            '''

lst=[]
for num in range(0,20):
    lst.append(num)
print(lst)

#############################################
#we can write same method using list comprehension  
#write list comprehension on interview page
lst=[num for num in range(0,20)]
print(lst)
###########################################
names=['dada','mama','kaka']
lst=[name.capitalize() for name in names]
print(lst)
###############################################
#list comprehension with if statement
def is_even(num):
    return num%2==0
lst=[num for num in range(10) if is_even(num)]
print(lst)
###################################################
lst=[f"{x}{y}"for x in range(3)for y in range(3)]
print(lst)

######################################################
#dictionary comprehenssion    #not gonna use as much like list
dict={x:x*x for x in range(3)}
print(dict)

##########################################################
#generator
#it is another way of iterating iterators in a simple way where it uses
#the keyword 'yield' 

gen =(x for x in range(3))
print(gen)
next(gen)
next(gen)
'''for i in range(0,10,2):
    yield i'''




















####################################################################
gen=(x for x in range(3))
next(gen)
next(gen)

####################################################################
#function which returns multiple values
def range_even(end):
    for num in range(0,end,2):
        yield num
for num in range_even(6):
    print(num)

##############################################################
#now istead of using for loop we can write our own generator
gen=range_even(6)
next(gen)
next(gen)
next(gen)
###########################################################
#chaining generator
def lengths(itr):
    for ele in itr:
        yield len(ele)
        
def hide(itr):
    for ele in itr:
        yield ele*'*'
        
''' ele* apperas to be placeholder for an element from an iterable. the 
asterik(*) is likely just a character used to represent a placeholder 
or a wildcard.
for instance , if you are iterating over a list of elements, "ele*"
could symbolize any element i that list. Its a genereic representation
that doesen't correspond to any specific syntax in python or itertools.

'''
password=['not-good','give m-pass','00100=100']

for password in hide(lengths(password)):
    print(password)
    
#############################################################
#enumerate
#printing list with index
lst=["milk","egg","bread"]
for index in range(len(lst)):
    print(f"{index+1} {lst[index]}")
#############
#same code can be executed using enumerator
lst=["milk","egg","bread"]
for index,item in enumerate(lst,start=1):
    print(f"{index} {item}")
    
##########################################################
#use of zip function
name=["dada","mama","kaka"]
info=[9850,6032,9785]
for nm,inf in zip(name,info):
    print(nm,inf)
    
#############################
#use of zip fnction with mis match list
name=["dada","mama","kaka","baba"]
info=[9850,6032,9785]
for nm,inf in zip(name,info):     #will not show baba
    print(nm,inf) 
    
######################
#zip_longest
from itertools import zip_longest
name=["dada","mama","kaka","baba"]
info=[9850,6032,9785]
for nm,inf in zip_longest(name,info):  #show baba with none
    print(nm,inf) 
    
#use of fill instead none
from itertools import zip_longest
name=["dada","mama","kaka","baba"]
info=[9850,6032,9785]
for nm,inf in zip_longest(name,info,fillvalue=0):  #show baba with 0
    print(nm,inf) 
    
#################################
#use of all(), if all values are true then it will produce output
lst=[2,3,-6,8,9]  #value must be non zero, wit can be +ve or -ve
if all(lst):
    print("all values are true")
else:
    print("there are null values")
    
###################
lst=[2,3,0,4,5,60]
if all(lst):
    print("all values are true")
else:
    print("there are null values")
    
##########################
#use of any(), if any one value is non zero
lst=[0,0,0,0,6,0,0,0]
if any(lst):
    print("it has some value")
else:
    print("all values are zero in the list")
    
##############################################
#count()
from itertools import count
counter=count()
print(next(counter))
print(next(counter))
print(next(counter))

################################################
#cycle()
#suppose you have repeated task to be done, then you

import itertools
instructions=("eat","code","sleep")
for instructions in itertools.cycle(instructions):
    print(instructions)
##################################################
#repeat()
from itertools import repeat
for msg in repeat("keep patience: ",times=3):
    print(msg)
    
###############################################
#combinations()
from itertools import combinations
players=["john","jani","janardhan"]
for i in combinations(players, 2):
    print(i)
    
################################################
#permutations()
from itertools import permutations
players=["rehan","samir","attar","bhoye",]
for i in permutations(players, 3):
    print(i)
    
###############################################
#product()
from itertools import product
team_a=['rohit','pandya','bumrah']
team_b=['virat','manish','shami']
for pair in product(team_a,team_b):
    print(pair)
    
##############################################
age=[27,17,19,21]
adult=filter(lambda age:age>=18,age)
print([age for age in adult])


##############################################################################

#INTERVIEW
''' inn python assif=gnment statement (a=b) did not create it only creates
its anoother object with same refernece means if yo change any this it will affect 
the original also. So in order to make a copy to not affect our original content,
we have to be very carefull.

for  'real' copies we can use the copy module.
however,for compound/nested objects(e.g. nested lists or dict and custom objects
   ) there is important diffecrence between shallow and deep copying:
    
    
    [shallow copies]:- only one level deep. it creteas an  new collector
    and poppulates it with reference to the nested object.
    this means modifying a nested object in the copy deeper tha ooone level causes
    modificationn in original also.
    lst=[1,2,3,4]     1-level deep
    lst=[[1,2,3,4]]    2-level deep
    
    [deep copies]:- a full independent clone. it creates a new 

'''


#assignment operation
#this will only create a new variable with the same reference.
list_a=[1,2,3,4,5,6]
list_b=list_a

list_a[0]=-10
print(list_a)
print(list_b)

########################################################
#shallow copy
#one level deep, Modifying on level 1 does not affect the original
#use copy.copy() , or object specific copy function

import copy
list_a=[1,2,3,4,5]
list_b=copy.copy(list_a)

#not affects the other list
list_b[0]=-10
print(list_a)
print(list_b)
#[1, 2, 3, 4, 5]
#[-10, 2, 3, 4, 5]
##########################################
'''26/3'''
#but with nested objects, modifying on level 2 or deeper
import copy
list_a=[[1,2,3,4,5],[6,7,8,9,10]]
list_b=copy.copy(list_a)

#it affects the other
list_a[0][0]=-10
print(list_a)
print(list_b)
##############################################
#deep copies
#full independent clones, use copy.deepcopy()

import copy
list_a=[[1,2,3,4,5],[6,7,8,9,10]]
list_b=copy.deepcopy(list_a)

#not affects the other
list_a[0][0]=-10
print(list_a)
print(list_b)
#[[-10, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
#[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]

#################################################
