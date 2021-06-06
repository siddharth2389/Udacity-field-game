import time
import random

# Define who the deamon is going to be and what the current weapon the player
deamon = random.choice(["dragon", "wicked fairie", "pirate"])
weapon = "dagger"


# Take 2 seconds pause after printing the statement
def print_pause(string):
    print(string)
    time.sleep(2)


# Initial setup for the game. Only used when the game is started or restarted
def intro():
    print_pause("You find yourself standing in an open field, filled with"
                " grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {deamon} is somewhere around here, and "
                "has been terrifying villagers.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective)"
                " dagger.\n")


# Defines what happens in the cave
def cave():
    global weapon  # define global variable
    if weapon == "dagger":
        print_pause("You cautiously peak into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical sword of Ogoroth!")
        print_pause("You discard your silly old dagger and take the sword with"
                    " you.")
        print_pause("You walk back to the field.")
        weapon = "sword"
        action_door()
    else:
        print_pause("You peer cautiously into the cave.")
        print_pause("You have been here before, and gotten all the good stuff."
                    " It's just an empty cave now.")
        print_pause("You walk back out into the field.")
        action_door()


# Defines what to say if you approach the house with dagger
def approach_with_dagger():
    global weapon
    print_pause("You approach the door of the house.")
    print_pause(f"You are about to knock when the door opens and out steps"
                f" a {deamon}.")
    print_pause(f"Eep! This is the {deamon}'s house.")
    print_pause(f"The {deamon} attacks you.")
    if weapon == "dagger":
        print_pause("You feel a bit under-prepared for this, what with only"
                    " having a tiny dagger.")


# Defines what to say if the player fights or runs away
def flight_fight():
    global weapon
    choice = int(input("Would you like to (1) fight or (2) run away?\n"
                       " (Please enter 1 or 2.)\n"))
    if choice == 1:
        if weapon == "sword":
            print_pause(f"As the {deamon} moves to attack, you unsheath your"
                        " new sword.")
            print_pause("The sword of Ogoroth shines brightly in your hand as"
                        " your brace yourself for the attack.")
            print_pause(f"But the {deamon} takes one look at your shiny new "
                        "toy and runs away!")
            print_pause(f"You have rid the town of the {deamon}. You are"
                        " victorious!")
            ask_play_again()
        else:
            print_pause("You do your best.")
            print_pause(f"But your dagger is no match for the {deamon}")
            print_pause("You have been defeated.")
            ask_play_again()
    elif choice == 2:
        print_pause("You run back into the field. Lucklily, you don't seem to"
                    " have been followed.")
        action_door()
    else:
        print_pause("Sorry I do not understand.")
        flight_fight()


# Defines what actions the player can take at the door
def action_door():
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    choice = int(input("What would you like to do?\n"
                       "(Please enter 1 or 2.)\n"))
    if choice == 1:
        approach_with_dagger()
        flight_fight()
    elif choice == 2:
        cave()
    else:
        print_pause("Sorry I do not understand.")
        action_door()


# Asks whether to play the game again
def ask_play_again():
    global deamon  # define that the variable is global
    global weapon  # identify that the variable is global
    choice = input("Would you like to play again? (y/n) \n").lower()
    if choice == "y":
        print_pause("Excellent! Restarting the game....")
        deamon = random.choice(["dragon", "wicked fairie", "pirate"])
        weapon = "dagger"
        deamon_gameplay()
    elif choice == "n":
        print_pause("Ok terminating the game.")
    else:
        print_pause("Sorry I do not understand")
        ask_play_again()


# Defines the final gameplay
def deamon_gameplay():
    intro()
    action_door()


deamon_gameplay()
