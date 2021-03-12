#!/usr/bin/env python3

#1 print first name and last name
print(f"Name: Mahlet Amare")

#2, initialize dic name password-database 
password_database = {"username":"dnedry", "password": "please"}

#3 initialie dic name command_database 
command_database = {"reboot":"OK. I will reboot all park systems.", "shutdown":"OK. I will shut down all park systems.", "done":"I hate all this hacker stuff."}

#4 initialize two objects named white_rabbit_object and counter
white_rabbit_object = 0
counter = 0

#create a while loop

while(white_rabbit_object == 0 and counter < 3):
  input_user= input("please enter the user name: ")
  input_password = input("please enter the password: ")
  counter += 1
  
  if counter == 3:
     print(f"You dind't say the magic word. {counter}")
     break
  
  if (input_user == password_database.get("username")) and \
     (input_password == password_database.get("password")):
     
     white_rabbit_object = 1       
     print("Hi, Dennis. You're still the best hacker in Jurassic Park.")    

     user_input = input("plese enter a commnand , reboot, shutdown or done: ")
     if(user_input == 'reboot'):
       print(command_database.get("reboot"))
       break  
     if(user_input == 'shutdown'):
       print(command_database.get("shutdown"))
       break
     if(user_input == 'done'):
       print(command_database.get("done"))    
       break
     else:
       print("The Lysine Contingency has been put into effect")
       break
     
     
      
