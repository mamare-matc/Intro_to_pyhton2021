#!/usr/bin/env python3

import subprocess

myProc = subprocess.run(['ps', '-axco', 'command'], stdout=subprocess.PIPE)

#decode to extract the string data 
myProcString = myProc.stdout.decode()
print(myProcString)

#split to creat a list from the decode data
myProcList = myProcString.split('\n')
print(myProcList)

#count munber of process in the list 
del myProcList[0]
print(len(myProcList))

#for loop to print one line at a time 
for newlist in myProcList:
    print (newlist)