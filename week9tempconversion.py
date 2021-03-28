#!/usr/bin/env python3
from c2f import celsius_to_fahrenheit
from f2c import fahrenheit_to_celsius

#Ask the user to enter the temprature and measure 
source_temp = float(input("Enter the temprature: "))
measure = input("select (F) for fahrenheit or (C) for celsius: " )

#Evaluate user inut and call the functions from the imported scripts and print the outpur
if measure == "F":
    print(fahrenheit_to_celsius(source_temp))
    
        
elif measure == "C":
    print(celsius_to_fahrenheit(source_temp))
         
else:
    print("Needs to be (F) or (C): ")

