# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 08:36:43 2024

@author: viren
"""

'''Exercise 1: Mailing Address

Write a program that displays your name and complete mailing address formatted in
the manner that you would usually see it on the outside of an envelope. Your program
does not need to read any input from the user.
'''

def my_adress():
    name = "Virendra Ghule"
    street_address = "SCOE,kopargaonn"
    city = "Kopargaon"
    state = "Maharshtra"
    postal_code = "413601"
    country = "India"

    print(name)
    print(street_address)
    print(city+" "+state+" "+postal_code+" ")
    print(country)

my_adress()


'''Exercise 2:Area of a Room

Write a program that asks the user to enter the width and length of a room. Once
the values have been read, your program should compute and display the area of the
room. The length and the width will be entered as floating point numbers. Include
units in your prompt and output message; either feet or meters, depending on which
unit you are more comfortable working with.
'''

def room_area():
    print("enter all values in meteres")
    l=float(input("enter length of room: "))
    b=float(input("enter breadth of room: "))
    area=l*b
    print("area of the rectangular room is: ",area,"sq.m")
    
room_area()

'''Exercise 3:Area of a Field

Create a program that reads the length and width of a farmer’s field from the user in
feet. Display the area of the field in acres.
Hint: There are 43,560 square feet in an acre.
'''

def area_acres():
    print("enter all data in feets")
    l=float(input("enter length of field: "))
    b=float(input("enter breadth of field: "))
    area=l*b
    acres=area/43560
    print("area of the filed in acres is: ",acres,"acres")
    
area_acres()

'''Exercise 4: Bottle Deposits

In many jurisdictions a small deposit is added to drink containers to encourage people
to recycle them. In one particular jurisdiction, drink containers holding one liter or
less have a $0.10 deposit, and drink containers holding more than one liter have a
$0.25 deposit.
Write a program that reads the number of containers of each size from the user.
Your program should continue by computing and displaying the refund that will be
received for returning those containers. Format the output so that it includes a dollar
sign and always displays exactly two decimal places.
'''

cont1=int(input("enter no of 1 liter containers:"))
cont2=int(input("enter no of more than 1 liter containers:"))
total=round((cont1*0.10)+(cont2*0.25),3) 
print("total amount you get: ",total,"$")


'''Exercise 5:Tax and Tip

The program that you create for this exercise will begin by reading the cost of a meal
ordered at a restaurant from the user. Then your program will compute the tax and
tip for the meal. Use your local tax rate when computing the amount of tax owing.
Compute the tip as 18 percent of the meal amount (without the tax). The output from
your program should include the tax amount, the tip amount, and the grand total for
the meal including both the tax and the tip. Format the output so that all of the values
are displayed using two decimal places.
'''

def restaurant():
    meal_cost=float(input("Enter meal cost: "))
    
    tip=round((meal_cost*0.18),2)
    
    tax=round((meal_cost*0.9),2)
    
    total=round((meal_cost + tip +tax),2)
    
    print('meal cost: ',meal_cost)
    print("tip:",tip)
    print('tax: ',tax)
    print('total: ',total,'$')
    
restaurant()
    
'''Exercise 6:   Height Units

Many people think about their height in feet and inches, even in some countries that
primarily use the metric system. Write a program that reads a number of feet from
the user, followed by a number of inches. Once these values are read, your program
should compute and display the equivalent number of centimeters.
'''

def height():
    case=int(input("enter your height: enter 1 for feet and 0 for inches: "))
    if case==1:
        feet = float(input("Enter the number of feet: "))
        height=feet*30.48
        print('height: ',height,'cm')
    elif case==0:
        inches = float(input("Enter the number of inches: "))
        height=inches*2.54
        print('height: ',height,'cm')
        
height()
