#!/usr/bin/env python3

print(f"Mahlet Amare")

with open("slicing-file.txt", "r") as hFile:
  listfile = hFile.readlines()
  
# Get the third word from the end of the list
  word1 = listfile[-3]
  aword1 = word1.replace('\n', '')
  print(aword1)

# Get the third through fifth word of the list
  word2 = listfile[2:5]
  s = " "
  nword2 = (s.join(word2))
  anword2 = nword2.replace('\n', '')
  print(anword2)
  
# Get the 10th word from the end of the file and every other word for 3 words
  o = " "
  word3 = listfile[-10:12:-2]
  nword3 = (o.join(word3))
  anword3 = nword3.replace('\n', '')
  print(anword3)

# Get the 11th though 13th word
  y = " "
  word4 = listfile[10:13]
  nword4 = (y.join(word4))
  anword4 = nword4.replace('\n', '')
  print(anword4)
# Get the 19th-21st words from the end of the file
  w = " "
  word5 = listfile[-19:-22:-1]
  nword5 = (w.join(word5))
  anword5 = nword5.replace('\n','')
  print(anword5)
# Create qoute and concatinate all the variables
  qoute = aword1 + " " + anword2 + " "+ anword3 + " " + anword4 + " " +  anword5 
  print(qoute) 
   
 
