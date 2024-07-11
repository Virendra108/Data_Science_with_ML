# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 09:37:05 2024

@author: viren
"""

print("hello world")
import math as ma
a=ma.pi
b=5
#########Session 2############
"""the input() function always take imput as string
by default. 
in order to convert it in to desired type we need to
specify type   to convert it into. for example if we 
want int then will take input as int(input()).this 
will convert the string into int"""
print(b)
age=input("enter your age:")
print(type(age))
age1=input("enter your age:")
print(type(age1))
age4=age+age1
print(age4)
print(type(age4))
age2=int(input("enter your age:"))
print(type(age2))

age1=int(input('please enter your age:'))
print(type(age1))
print(age1)

age2=int(input('enter your age: '))
print(type(age2))
print(age2)
age=age1+age2
print(age)
print(type(age))
'''TAKEAWAY: 
    '''
######################################################
#coverting to floats
int_value=100
string_value='1.5'
float_value= float(int_value)
print('int value as float:',float_value)
print(type(float_value))
float_value=float(string_value)
print('string value as a float:',float_value)
print(type(float_value))
####################################################
#Complex numbers
c1=1
c2=2j
print('c1:',c1,'c2:',c2)
print(type(c1))
print(type(c2))
print(c1.real)
print(c2.imag)
print(c2.real) #give 0.0 as value
#####################################################
#Boolean values
#a Boolean type can only be having one of these values as True or  False
all_ok=True
print(all_ok)
all_ok=False
print(all_ok)
print(type(all_ok))
#####################################################################
#You can also covert strings into Boolean
#True or False (and nothing else)
status=bool(input('OK it is confirmed? :'))
print(status)
print(type(status)) #will return true if you give any input as y/n
                    #to get false just dont give input i.e false for n
#######################################################################
#Arithematic Operators
#for add,sub,mul===> result is INT
#for division===>result id FLOAT by default
home=10
away=15
print('home+away=',home+away)
print(type(home+away))
print('10*4=',10*4)
print(type(10*4))
print('20/5=',20/5)

#io order to print int in division we can use //
print('20//5=',20//5)
print(type(20//5))
########################################################################4
'''             Session 03   19march               '''

'''power operator'''
a=5
b=3
print(a**b)
#########################################################################
'''Assignment operator'''
x=5
x+=1
print(x)
###################################################
#none value(None Type)
#python has special value called none, the none type with a single
#value none

winner= None
print(winner is None)

print(winner is not None)
print(type(winner))

winner= None
print('winner:',winner)
print('winner is none:',winner is None)
print('winner is not none:',winner is not None)
####################################################################

'''indentation is very important in python, layout of the code is determined
by it.
indetattionn is used to determine how one piece of code sjould
be associated with another piece of code and how it wwll be executed.'''

num=int(input('enter a number:'))
if num>0:
print(num)

#now giving correct indentation
num=int(input('enter a number:'))
if num>0:
    print(num)
#using else in if
num=int(input('enter a number:'))
if num<0:
    print('its negative')
else:
    print('it is positive')
    
#the use of elif
saving=float(input('enter your savings :'))
if saving==0:
    print('do some saving man !')
elif saving<500:
    print("are you new here !")
elif saving<1000:
    print('good start! ')
elif saving<5000:
    print("thats a tidy sum")
elif saving<10000:
    print('welcome sir!')    

###################################################################
'''the while loop exist in every programming languages and is used
to iterative (or repeat) one or more code statements as long as the
test condition (expression) is true.'''

count=1
print('starting')
while count<=10:
    print(count)
    count+=1
###############################################
#For loop
#prinnting or doing something in specified range
print('printin values in a specific range:')
for i in range(2,10):
    print(i)
    print('done')
    ########### MISSED PART TTTTTTTTTTTTTTTTTTTT##########
    
    
######################################################################
################# '''SESSIONN 4  20/3'''   ##############################
#python program to print odd and even numbers in given range
start ,end=4,19
for num in range(start,end+1):
    if num%2!=0:
        print(num,end=" ")
        
        
start ,end=4,19
for num in range(start,end+1):
    if num%2==0:
        print(num,end=" ")
    
#########################################################
x,y,z=1,3,5
print(x)
print(y)
print(z)
x,y,z=5
print(x)
print(y)
print(z)
#######################################################
#global variables
x='awesome'
def my_function():
    print("python is: "+x)
my_function()

#global and local variables
x='awesome'
def my_function():
    x='fantastic'
    print("python is: "+x)
my_function()
print("oython is a:"+x)    
#while writing code in a function priority given to local mor than
#global variable   i.e. local>global

##################################################################
#getting data  type
x=5
print(type(x))          #int
x=range(6)
print(type(x))          #range
x={"name":"Ram","age":34}
print(type(x))          #dict

######################################
str1="hello"
str2=5
str3=str1+str2 #gives error: string can =be concatenate with string only
#not with integer
###################################################################
#if you want multiple strings 


#When you enclose a string within triple quotes ("""), 
#you can include line breaks and create multi-line strings.
# Here's how you've assigned it:
y="this is python.
it is very powerfull"
x="""this is python 
it is very powerfull"""
print(y)
print(x)

####################################################################
#string slicing
x="""this is python.it is very powerful"""
#                             -5-4-3-2-1  e r f u l
print(x[2:8])  #end letter 8 not considered
#slicing from start
print(x[:3])
#slicing from the end
print(x[4:])   #all are consiidered even end letter
#negatttive indexing
print(x[-5:-2])

######################################################################
#modify string
print(x.upper())

x=x.upper()
print(x.lower())

#####################################################################
#rewmoving white spaces  (starting spaces)
x="     this is   python    "
print(x.strip())
print(x)
print(x.rstrip())

#replacing word in string
x="hello world"
print(x.replace("hello","gello"))

#use of split which replaces white sppaces
x="hello world"
print(x.split(" "))
#######################
x="hello world"
string1=x[::-2]
print(string1)
print(x[::-1])  #will print reverse of the line
########################
#find method, searches the string for a specified value and give its location
x="this is python and it is very powerfull"
print(x.find("and"))
############################
#to add white space
x="hello"
y="world"
print(x+" "+y)
#########################################################
'''String Format'''
x=36
y="my age is:"
print(x+y)    #will give error
print(f"my age is {x}")

quantity=3
item_no=54
price=67
print(f"I want {quantity} pieces and item number is {item_no}, Its price is {price}")

#another method
my_order="I want {} pieces and its number is {}, its orice is {}"
print(my_order.format(quantity,item_no,price))

my_order="I want {0} pieces and its number is {1}, its orice is {2}"
print(my_order.format(quantity,item_no,price))

####################################################################
#the escape character allows you to use double quotes when
text="This is fun fair and it has got big \"round rigo\"" 
print(text)


########################################################################
#operator precedence
print(3*3+3/3-3)
'''
rule for mathematical operations
PEDMAS
paraenthesis
expotential
multiplication
division
addition
subtraction'''
##################################################################3##
#python list
list=["cherry","banana","apple"]
print(list)
#list items are indexed, the first item has index [0]
print(list[0])
print(list[2])
#####################################################################
#appeend()    Adds an elemnt to thhe list
list=["cherry","banana","apple"]
list.append("Mango")
print(list)
#clear removes all the lement from the list
list.clear()
print(list)
#copy()method
list2=list.copy()
print(list2)
#######################
#count() returns the number of times the vlaue occured in list
lst=["cherry","cherry","banana"]
lst.count("cherry")
###############################################
#extend() add the elements of list to another list
lst=[1,2,3]
lst2=[4,5,6]
lst.extend(lst2)
print(lst)
###############################################
#insert() method, insert the value at the specified position
lst.insert(1, "mango")
print(lst)
###############################################
#pop() removes the element at specified position
lst.pop(0)
print(lst)

#remove() method removes the element with specified value
lst=["cherry","cherry","mango"]
lst.remove("cherry")
print(lst)

###############################################
#to reverse order of the list
lst=["cherry","cherry","mango"]
lst.reverse()
print(lst)
###############################################
'''list sorting'''
#list_name.sort()
lst=["cherry","orange","banana"]
lst.sort()
print(lst)
###############################################


"""     TUPPLE()    """
#written in parenthesis
tup=("cherry","cherry","banana")
print(tup)
print(tup[2])
##################################################
#immutable: once a tuple is created, you cannot change its values
x=("apple","banana","cherry")
#x[1]='kiwi'

#inoorder to change we have to first convert it into list
y=list(x)       #giving error as we declared variable name list above
y[1]='kiwi'
#again revert it into tuple
x=tuple(y)
print(x)
####################################################
x=("apple",2,"cherry")
print(x)
#########################################
#you can acess tupple value by refering the index
x=("apple","banana","cherry")
print(x[1])
###########################################
#to join two or more tuples you can use the + operator
tup1=("a","b","c")
tup2=(1,2,3)
tup3=tup1+tup2
print(tup3)

############################################################################
'''    DICTIONARY   '''
# it have keys and values
dict1={"Brand":"Maruti","model":"2345","year":2011}
print(dict1)
print(len(dict1))    #will print how many key value pairs are there


dict2={"Brand":["Maruti","Mahindra","Toyota"],
       "Model":["a","b","c"],
       "Year":[2011,2013,2022]}
print(dict2)
#############################################
dict1={"Brand":"Maruti","model":"2345","year":2011}

dict1.get("model")

dict1.keys()


###########################################################################
'''------------------------------------------------------
--------------6th session, 21-03-2024------------
------------------------------------------------------'''

car={"Brand":"Ford","Model":"Mustang","Year":"1964"}
x=car.keys()
print(x)
car["color"]="White"
#car
x=car.keys()
print(x)

#Removing Dictionary element

car={"Brand":"Ford","Model":"Mustang","Year":"1964"}
car.pop("Brand")
print(car)

#Accessing keys from dictionary 
for x in car:
    print(x)
    
#Accessing values from dictionary
for x in car:
    print(car[x])

#if you want to access both keys and values(VI)
for key,value in car.items():
    print("%s=%s" %(key,value))
    
#copying the dictionary
car={"Brand":"Ford","Model":"Mustang","Year":"1964"}
car2=car.copy()
car2
print(car2)

#Another way to make a copy of dictionary
thisdict={"Brand":"Ford","Model":"Mustang","Year":"1964"}
dict1=dict(thisdict)
print(dict1)

#A dictionary can contain dictionaries this is called'
#as nested dictonary
our_family={"Child":{ "Name":"Ram","Dob":"02-12-2000"},
           "Child2":{"Name":"Sham","Dob":"03-04-2000"}}
print(our_family)

#clear() removes all elements from the car

car={"Brand":"Ford","Model":"Mustang","Year":"1964"}
car.clear()
print(car)

#create a dictionary from key method
x={'key1','key2','key3'}
y=0
thisdict=dict.fromkeys(x,y)
print(thisdict)
       
#get()=to get values from dictionary
car={"Brand":"Ford","Model":"Mustang","Year":"1964"}
car.get("Model")

#items()=returns thr dictinary's key-value
car={"Brand":"Ford","Model":"Mustang","Year":"1964"}
car.items()

#values()=Display all values od dictionary
car={"Brand":"Ford","Model":"Mustang","Year":"1964"}
car.values()

#update()=insert item in dictionary
car={"Brand":"Ford","Model":"Mustang","Year":"1964"}
car.update({"color":"white"})
print(car)

--------------------------------------------------
#for loop
fruits=["Apple","Banana","cherry"]
for i in fruits:
    print(i)
    
#use of break statement
fruits=["Apple","Banana","cherry"]
for i in fruits:
    #print(i)
    if (i=="Banana"):
        break
    print(i)
    
fruits=["Apple","Banana","cherry"]
for i in fruits:
    if (i=="Banana"):
        break
    print(i)
    
#use of continue statement
fruits=["Apple","Banana","cherry"]
for i in fruits:
    print(i)
    if (i=="Banana"):
        continue

fruits=["Apple","Banana","cherry"]
for i in fruits:
    if (i=="Banana"):
        continue
    print(i)
    
    
    
    
    
    
'''-----------------------------------------------------=======================
=======================================================================    
'''

'''    21/3  afternoon session    '''

#range function
for x in range(2,6):
    print(x)
#will go from 2 to 6  but not give 6 as it is stopped at 6

#to give incrementation condition in it
for x in range(2,30,3):
    print(x)
    

###############################################################
#nested loop :- loop inside loop
colors={"green","yellow","red"}
fruits={"guava","banana","apple"}
for x in colors:
    for y in fruits:                
        print(x,y)              #will give revert for dict
        
        
colors=["green","yellow","red"]
fruits=["guava","banana","apple"]
for x in colors:
    for y in fruits:
        print(x,y)               #order wise for list
              

##################################################################
#function
def my_function():
    print("hello from the function")
my_function()


def my_function(name):
    print("hello "+name)
    
my_function("ram")

def my_function(name1,name2):
    print(name1 +" "+name2)
my_function("hello", "world")
my_function("world", "hello")

###################################################################
#Arbitery Arguments , *args
#if you dont know how many arguments that will be passed into your
#function , add a * before parametre name in the function definition.
def my_function(*kids):
    print(kids[0]+" "+kids[2])
    
my_function("hello","world","India")

###################################################################
#kwargs
'''a keyword agrument is where you  provide  an me to vairab le functiona being a dictionary
two asterik givven to it'''

'''**kwargs in Python is a special parameter that allows you to pass a 
variable number of keyword arguments to a function. It collects these
 arguments into a dictionary within the function, where each keyword 
 argument becomes a key-value pair. This flexibility enables functions to 
 accept any number of additional arguments without needing to 
 explicitly define them in the function signature.'''



ef myfun(**kwargs):                       #you can use different keyword also
    for key, value in kwargs.items():
        print("%s == %s"%(key,value))

myfun(first="popatlal", mid="mohanlal",last='goyal')

################################################################
#the following example shows how to use a defalut parametre 
#if argument passed it will be printed
#BUT if argument is not passed the default value will be used

def my_function(country="norway"):
    print("I am from "+ country)
    
my_function("india")
my_function()          #default value will be used

#################################################################
#passinng list as argument 
#you can send any data types of argument to the function
#e.g. if you send a list  as argument , it will still

fruits=["orange","banana","guava"]
def my_function(fruits):
    for x in fruits:
        print(x)
        
my_function(fruits)
#################################################################
#return Values
#to let a function reurn a value, use the return statement
def my_function(x):
    return x*5
my_function(10)
#########################################
#pass functions
def my_function():
    pass
#having an empty function definition
#it will raise an error without the pass statement



#factorial of a number
def factorial(x):
    if x==1:
        return 1
    else:
        return(x*factorial(x-1))
    
factorial(3)
factorial(5)
factorial(6)
factorial(720)

##################################################################
#A LAMBDA function also called anonymous function
'''important for interview purpose'''
#a lambda function can take any number of arguments
#but can only have one expresssion
def add(a):
    sum=a+10
    return sum
add(20)

add= lambda a:a+10
print(add(20))

#lambda function can take any number of arguments
add1= lambda a,b,c:a+b+c
print(add1(10,11,12))

######################################
#finding odd numbers from the list

#the  filter() method accepts two arguments:
    #a function and an iterable such as a list
    #the function is for every iterable of the list
    #and a new iterable or list is returned that holds just
    #those elements that returned true whhen supplied to the
lst=[34,12,64,55,75,13,63]
odd_list=list(filter(lambda x:(x%2 !=0), lst))
print(odd_list)            

even_list=list(filter(lambda x:(x%2==0),lst))  
print(even_list)


sqr_list=list(filter(lambda x:(x**2),lst))  
print(sqr_list)

sqr_list=[x**2 for x in lst]
print(sqr_list)

sqlst=[]
a=lambda x:x**2
for x in lst:
    sqlst.append(a(x))
print(sqlst)

#the correct method
sqr_lst=list(map(lambda x:(x**2),lst))
print(sqr_lst)
###################################################################
 ''' 22/3  morning session'''
 #use cases
 #roller coster problem
 print("Welcome to the roller coaster")
 height=int(input("Enter your height in cm:"))
 if height>=120:
     print("you are eligibke for roller coaster rides!")
     age=int(input("enter your age in years: "))
     bill=0
     if 16<=age<=10:
         print("childs ticket is 5$: ")
         bill+=5
     elif 16<age:
         print("adults ticket is 8$")
         bill+=8
     else:
         print("you are under age !")
 print("you have to pay:",bill,"$")
 else:
     print("you are not eligible. as height must be more than 120 cm")
