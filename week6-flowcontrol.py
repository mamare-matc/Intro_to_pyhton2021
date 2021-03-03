#!/usr/bin/env python3 

print("""You enter a dark room with three doors. 
Do you go through door #1 or door #2 or door #3?""")


door = input("-> ")

# == Door Number 1 logic =======================
if door == "1":

    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?\n")

    print("1. Take the cake.")
    print("2. Scream at the bear.")

    # == Bear logic ============================
    bear = input("-> ")

    if bear == "1":
        print("1) The bear eats your face off. Good job!")
    elif bear == "2":
        print("2) The bear eats your legs off. Good job!")
    else:
        print(f"N)Well, doing {bear} is probably better.")
        print("Bear runs away.")

# == Door Number 2 Logic =====================
elif door == "2":
    print("You will see the huge screen with a horror movie you don't like.\n")
    print("what will you do?")
    
    print("1. Go back.")
    print("2. Change the movie.")
    print("3. close your eyes.")
    
    # == Insanity Logic ======================
    insanity = input("-> ")

    if insanity == "1" or insanity == "2":
        print("1) You can't go back the door is closed and can't change it.")
        print("2) Try that,  Good luck!")
    else:
        print("3) That is a better thing to do.")
        print("N) Good job!")

# Door Number 3 logic 
elif door == "3":
    print("There is a surprise party.\n what would you do?")

    print("1. will you join the party")
    print("2. run away")

    #party logic
    party = input("-> ")

    if party == "1":
        print("1. Enjoy the party")
    elif party =="2":
        print("2.  sorry you missed it it's your birthday")
    else:
        print(f"N)sorry, you did {party} the party is over")

else:
    print("You did not select a door?? Good call :)")
