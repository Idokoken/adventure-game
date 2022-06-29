import time
import random

#pause fuction
def print_pause(msg):
   print(msg)
   time.sleep(2)

#intro part
def intro():
    print_pause("You find yourself " "standing in an open field,") 
    print_pause("filled with grass and " "yellow wildflowers.")  
    print_pause("Rumor has it that a " "wicked fairie is somewhere around here,") 
    print_pause("and has been terrifying " "the nearby village.")


#getting user input
def main(): 
    print_pause("Enter 1 to knock on the door of the house.")    
    print_pause("Enter 2 to peer into the cave.")    
    print_pause("What would you like to do?")
    resp = input("Please enter 1 or 2")
    if int(resp) == 1:
        print_pause("you knocked on the door")
    elif int(resp) == 2:
        print_pause("u peered into the cave")
    else:
        print_pause("try again")
        main()
        
def play_game():
    main()
    
play_game()

   