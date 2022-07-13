import time
import random


# pause fuction
def print_pause(msg):
    print(msg)
    time.sleep(2)


enemy = ["Pirate", "Gordon", "wicked Fairie", "Dragon"]


# won fight
def win():
    print_pause("As the pirate moves to attack, you unsheath your new sword.")
    print_pause("The Sword of Ogoroth shines brightly in your hand as you "
                "brace yourself for the attack.")
    print_pause("But the pirate takes one look at your shiny new toy and "
                "runs away!")
    print_pause("You have rid the town of the pirate. You are victorious!")
    play_again()


# lost fight
def lost():
    print_pause("You do your best...")
    print_pause("but your dagger is no match for the wicked fairie.")
    print_pause("You have been defeated!")
    play_again()


# play again
def play_again():
    print_pause('GAME OVER')
    play = input("Would you like to play again? (y/n) ")
    if play.lower() == 'y':
        print_pause("Excellent! Restarting the game ...")
        play_game()
    elif play.lower() == 'n':
        print_pause("Thanks for playing! See you next time.")
    else:
        play_again()


# intro part
def intro():
    print_pause("You find yourself standing in an open field, filled with "
                "grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {random.choice(enemy)} is somewhere "
                "around here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective) "
                "dagger.\n\n")


# fight_or_run
def fight_or_run():
    what_to_do = input("Would you like to (1) fight or (2) run away?")
    if what_to_do == "1":
        lost()
        # win()
    elif what_to_do == "2":
        print_pause(
            "You run back into the field. Luckily, you don't seem to "
            "have been followed.")
        action()
    else:
        fight_or_run()


# action
def action():
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    main()


# getting user input
def main():
    resp = input("(Please enter 1 or 2).\n")
    if resp == '1':
        print_pause("you knocked on the door")
        print_pause("You approach the door of the house.")
        print_pause(
            "You are about to knock when the door opens and out steps a"
            " pirate.")
        print_pause("Eep! This is the pirate's house!")
        print_pause("The pirate attacks you!")
        print_pause("You feel a bit under-prepared for this, what with "
                    "only having a tiny dagger.")
        fight_or_run()

    elif resp == '2':
        print_pause("you peered into the cave")
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause(
            "You discard your silly old dagger and take the sword with you.")
        print_pause("You walk back out to the field.")
        play_again()
    else:
        main()


def play_game():
    intro()
    action()


play_game()
