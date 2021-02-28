#!/usr/bin/env python3

#1a use the len() function to get the size and print it out to the screen to str 
hFile = open("/etc/passwd", "r")
strfiletext = hFile.read()
print(strfiletext)
print(type(strfiletext))
print("Total length of the characters: ", len(strfiletext))
hFile.close()

#1b Add a print statement to your script to indicate what the len() function counts str 
print("the lel() funtion counts 3040 bites for string")

#1c Add a print statement to your script to describe when would you use this technique str 
print("I would use this technique to open the file with read only mode 'r' and print the type and the length of the file in bites")

#2a use the len() function to get the size and print out to the screen  list 
hFile = open("/etc/passwd", "r")
listfiletext = hFile.readlines()
print(listfiletext)
print(type(listfiletext))
print("Total number of list: ", len(listfiletext)) 
hFile.close()

#2b add a print statement to your script to indicate what the len() function  counts list 
print("The len() function counts 53 list")

#2c add a print statement to your script to describe when would you use this technique list 
print("I would use this technique in order to read the list using readlines to output the content of the file as a list, by using readlines() to read the list and using len() function to get the number of list ")

#3a the len() function will not work here. Add code that will calculate the total length of the file and print it out to the screen 
count = 0

with open("/etc/passwd", "r") as hFile:
  linefiletext = hFile.read() 
  while linefiletext:
   print(linefiletext)
   count += 1
   print("Total length of characters: ", len(linefiletext))
   break
print("I would use this technique in order to read a file one line at a time and also count the number of characters in the content using while loop, the loop iterates every line and increaments and print len() prints the total number of the characters and when reading file is done break will stop the loop")

#3b add a print statement to your script to describe when would you use this technique 




