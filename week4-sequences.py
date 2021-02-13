#!/usr/bin/python3

varString = "Here is a nice string to slice"
varTuple = ("Here","is","a","nice","tuple","to","slice")
varList = ["Here","is","a","nice","list","to","slice"]

#a print e is a nice string to slice from varString 
print(varString[3:30])

#b Her from varString
print(varString[:3])

#e is a ni from varString
print(varString[3:12])

#d Hr sanc tigt Ic from varString
print(varString[0:30:2])

#e print eclis ot gnirts ecin a si Here from varString  
print(varString[::-1])

#a reverse the varList
print(varList[::-1])

#b pring a, is, Here
print(varList[2::-1])

#c print a, nice
print(varList[2:4])

#d print  Here, nice, slice
print(varList[0::3])

#e print is, a, nice. list. to, slice 
print(varList[1:])

#using a for loop, print out each element of varString one line at a time 
for element in varString:
    print(element)

#using a for loop, print out each element of varList	
for element in varList:
    print(element)
