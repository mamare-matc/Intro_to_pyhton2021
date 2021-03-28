#!/usr/bin/env python3

#convert fahranheit to  celsius

def fahrenheit_to_celsius(fahrenheit):
    solve = (fahrenheit - 32) * 5/9
    return solve

def main():
   user_input = float(input('Enter temp in fahrenheit : '))
   print(round(fahrenheit_to_celsius(user_input), 0))

main()
