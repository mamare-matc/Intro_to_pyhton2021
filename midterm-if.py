#!/usr/bin/env python3
print(f'Name: Mahlet Amare')

Total = 0
linenumber = 0

#3.1 Read file and create Total variable and loop to extract the line number of the string add the number lines in Total 
with open("Midterm-if.txt","r") as hFile:

     for line in hFile:
      linenumber += 1

      if "gmeach18@ed.gov" in line:
        Total += linenumber
      if "248.253.63.149" in line:
        Total += linenumber 
      if "Whiteland" in line:
        Total += linenumber 
      if "80.222.19.190" in line:
        Total += linenumber
      if "Kayley" in line:
        Total += linenumber 
      if "dcassyqw@microsoft.com" in line:
        Total += linenumber  
        
        print(f" The total is: {Total}")   
  
