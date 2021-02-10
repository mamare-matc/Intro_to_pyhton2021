#!/usr/bin/python3

#week 3 srting formating assignment 

varRed = "Red"
varGreen = "Green"
varBlue = "Blue"
varName = "Timmy"
varLoot = 10.4516295

# 1 print a formatted version of varName
print(f"'Hello {varName}")

# 2 print multiple strings connecting with hyphon
print(f"'{varRed}-{varGreen}-{varBlue}'")

# 3 print strings concatnating with variable
print(f"'Is this {varGreen} or {varBlue}?'")

# 4 print string concatnating with varName
print(f"'My name is {varName}'")

# 5 print varRed by adding ++ 
print(f"'[++{varRed}++]'")

# 6 print varGreen adding == at the end
print(f"'[{varGreen.lower()}==]'")

# 7 print **** and varBlue
print(f"'[****{varBlue.lower()}]'")

# 8 print varBlue multiple time
print(f"'{varBlue}'"*10) 

# 9 print varLoot with single qoute
print(f"'{varLoot}'")

# 10 print varLoot using indexing to  get the first three numbers
print(round(varLoot, 1))

# 11 print  string concat with indexing varLoot
print(f"I have $" + str(round(varLoot, 2)))

# 12 print a formatted string that contais variables
print(f"'[$$${varRed}$$$$][$${varGreen}$$$][$$${varBlue}$$$]'")

# 13 print reversed string for varRed and varBlue 
print(f"'[ {varRed[::-1]} ][ {varGreen} ][ {varBlue[::-1]} ]'")

# 14 print string concattnating with variables
print(f"'First Color:[{varRed}]Second Color:[{varGreen}]Third Color:[{varBlue}]'")


