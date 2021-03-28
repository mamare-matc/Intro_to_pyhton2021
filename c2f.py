#!/usr/bin/env python3

#convert celsius to fahranheit  

def celsius_to_fahrenheit(celsius):
    result = (celsius * 9/5) + 32
    return result

def main():
   user_input = float(input('Enter temp in celsius : '))
   print(round(celsius_to_fahrenheit(user_input), 0))

main()
