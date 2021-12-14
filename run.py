# developer: Madelene Eriksson
# description: Text-based mystery adventure game
# name: Secret Legend

# Write your code to expect a terminal of 80 characters wide and 24 rows high

"""import time"""
import os
import sys


def lname():
    lname.upper()


def fname():
    fname.upper()


def clear_terminal():
    """
    clears the terminal from the information existing before.
    """
    os.system("clear")


def game_over():
    """
    When the player doesn't want to continue playing the game
    """
    print("---------------------------------------")
    print()
    print("Are you really sure you can't do better?")
    print()
    print("---------------------------------------")
    sys.exit()


def play_game():
    """
    This function is called when you start up the game.
    Works like a homepage. This function works on a
    global scale.
    """
    print()
    print(" -------------- LEGEND OF THE FAMILY CHEST -------------- ")
    print()
    print('''\033[31m
     =============================================================
                                  ___
                              ___(___)_______________
                        ______|                     |______
                      |       |                     |      |
                    _|_______ |_____________________|_______|_
                   |__________________________________________|
                    | ===================================== |
          __________|   _    _       _   _       _   _      |
         /__/__/__/_|  |_|  |_|     |_| |_|     |_| |_|     |
        /__/__/__/__|  |_|  |_|    _________    |_| |_|     |
        |===========|              |   /   |                |
        |__|__|__|__|              |___/___|                |
        |__|__|__|__|=============|_________|===============|
        |___________|____________|___________|______________|
        ========================|_____________|=============|

     ============================================================
    \033[0m\n''')

    print("Somewhere behind these walls lies the answer to the")
    print("legend about the family treasure. Are you ready to ")
    print("find the truth? (1 or 2):")
    print("--------------------")
    print("- 1 -  Hell yeah!")
    print("- 2 -  No, too much pressure..")
    print("---------------------")
    print()

    answer = input("").lower().strip()

    # Validation input
    while answer not in "1" and answer not in "2":
        print("You have to make a choice, please try again")
        answer = input("").lower().strip()
        continue
    if answer == "1":
        clear_terminal()
        print("---------------------------------------")
        print("Such a good answer, there is no time like the present!")
        print("---------------------------------------")
        global fname
        fname = input("What is your first name? \n")
        print("---------------------------------------")
        global lname
        lname = input("What is your last name? \n")
        print("---------------------------------------")
        print(f"Hello {fname} {lname}, we have been waiting for you..")
        print("---------------------------------------")
        introduction()
    elif answer == "2":
        clear_terminal()
        print("---------------------------------------")
        print("Oh I see, well an adventure is not for all")
        print("---------------------------------------")


def introduction():
    """
    Introducing a storyline for the player where they have the,
    opportunity to choose to embark on the adventure
    """
    clear_terminal()
    print(f"Growing up the famous treasure von - {lname} - was all you could")
    print("hear about. But when you asked where it was you never")
    print("got an answer. All they said was --you will find out")
    print("in good ol' time-- ")
    print()
    print("Well today was this day, because when you opened your")
    print("mail you were happy and surprised to find a funny looking")
    print("envelope with a sigil on the back.")
    print()
    print("You thought the information inside it was useless but")
    print("for some reason you couldn't get that sigil out")
    print("of your mind. It looked like a heart pierced by two daggers! ")
    print("When you turned the envelope you could see an address on the back.")
    print(f"This address might be the answer to the -{lname} -family legend..")
    print()
    print("---------------------------------------")
    print("-- 1 --  No time to lose, let's go!")
    print("-- 2 --  This adventure is not meant for me..")
    print("---------------------------------------")
    print()

    # Validation input
    answer = input("").lower().strip()
    while answer not in "1" and answer not in "2":
        print("You have to make a choice, please try again")
        answer = input("").lower().strip()
        continue
    if answer == "1":
        clear_terminal()
        print("Perfect!")
        start()
    elif answer == "2":
        clear_terminal()
        print("---------------------------------------")
        print("Oh I see, well an adventure is not for all")
        print("---------------------------------------")
        


def start():
    """
    Gives the player their first choice which will affect their journey
    """
    clear_terminal()
    print(f"After a couple of hours of traveling - {fname} - was standing")
    print("in front of a huge badly maintained mansion. So this was the")
    print(f" famous von - {lname} - manor. - {fname} - moved up the stairs")
    print("and pushed down the door handle. It worked!")
    print()
    print(f"- {fname} - walked inside and was overwhelmed by the interior.")
    print("It was such a beautiful place, why did our family ever leave?")
    print()
    print("There were two different doors that stood out, one leading to the")
    print("greenhouse and the other to the library.")
    print("---------------------------------------")
    print("What will be your choice? (1 or 2)")
    print("-- 1 -- Greenhouse")
    print("-- 2 -- Library")
    print("---------------------------------------")
    print()

    # Validation input
    answer = input("").lower().strip()
    while answer not in "1" and answer not in "2":
        print("You have to make a choice, please try again")
        answer = input("").lower().strip()
        continue
    if answer == "1":
        clear_terminal()
        print("---------------------------------------")
        print("Oh really, interesting choice..")
        print("---------------------------------------")
        greenhouse()
    elif answer == "2":
        clear_terminal()
        print("---------------------------------------")
        print("You head inside the library, but you have no")
        print(f"idea what to look for. - {fname} - searches for")
        print("hours but can't find anything. The day turns to night")
        print(f"and -{fname} finally accepts it is time to head home.")
        print("Hopefully my choices tomorrow is better.")
        print("---------------------------------------")
        game_over()
      

def greenhouse():
    """
    Continuing the storyline about the family chest together
    with a validation input
    """
    clear_terminal()
    print(f"- {fname} - navigated inside the greenhouse,")
    print("avoiding all the debris laying on the ground.")
    print(f"- {fname} - starts to move the flashlight up and down")
    print("and notices a spiral staircase hidden in the corner.")
    print()
    print("It is old and rusty and have a specific pattern ")
    print("engraved in the steel that reminds you of stars and moons")
    print(f"Suddenly a loud sound is heard behind - {fname} - and when you")
    print("start to turn around you see something move next to the fountain.")
    print()
    print("You can either continue and make your way to the staircase or")
    print("investigate what moved next to the fountain.")
    print("---------------------------------------")
    print("What will be your choice? (1 or 2)")
    print("-- 1 -- Staircase")
    print("-- 2 -- Fountain")
    print("---------------------------------------")
    print()

    # Validation input
    answer = input("").lower().strip()
    while answer not in "1" and answer not in "2":
        print("You have to make a choice, please try again")
        answer = input("").lower().strip()
        continue
    if answer == "1":
        clear_terminal()
        print("---------------------------------------")
        print(f"- {fname} - start to climb the staircase and as you are")
        print("making your way up you feel the stairs break underneath you.")
        print("You fall down and breaks both of your legs, you")
        print("know that you cannot continue and your adventure")
        print("is officially over. ")
        print("---------------------------------------")
        game_over()
    elif answer == "2":
        clear_terminal()
        print("---------------------------------------")
        print("You are not the scared type I see")
        print("---------------------------------------")
        fountain()


def fountain():
    """
    """
    clear_terminal()
    print(f"{fname} take a couple of steps forward with your heart pumping")
    print("through your chest. The sound came from underneath a large box")
    print("placed next to the fountain, after taking a deep breath")
    print("you decide to kick the box and a rat trapped underneath")
    print("makes you jump. When you calm down you see some types of symbols")
    print("engraved in the stone. Next to it you find a strange looking key.")
    print()
    print("After taking the key you take a look on the symbols on the ground.")
    print("You remove the mosss and you suddenly see something")
    print("resembeling a bookcase and the different moon phases.")
    print()
    print("You realise that it is something meant to be found inside")
    print(f"this house. {fname} decides that the symbol could only")
    print("point to two places.")
    print("---------------------------------------")
    print("What will be your choice? (1 or 2)")
    print("-- 1 -- Head to the staircase")
    print("-- 2 -- Move on to the library")
    print("---------------------------------------")
    print()

    # Validation input
    answer = input("").lower().strip()
    while answer not in "1" and answer not in "2":
        print("You have to make a choice, please try again")
        answer = input("").lower().strip()
        continue
    if answer == "1":
        clear_terminal()
        print("---------------------------------------")
        print(f"{fname} start to climb the staircase and as you are making")
        print("your way up you feel the stairs break underneath you.")
        print("You fall down and breaks both of your legs, you")
        print("know that you cannot continue and your adventure")
        print("is officially over. ")
        print("---------------------------------------")
        game_over()
    elif answer == "2":
        clear_terminal()
        print("---------------------------------------")
        print("You really got the hang of this!")
        print("---------------------------------------")
        library()


def library():
    """
    """
    clear_terminal()
    print("After taking your first steps inside the library you feel")
    print("a cold chill moving down your spine and you know instantly")
    print("that you are in the right place. You try to flip a switch")
    print("and to your relief a dim light turns on and you move towards")
    print("the bookcase. When you start to scan the titles you see an")
    print("astronomy book and your curiosity takes over.")
    print()
    print("You start to pull the book out when the picture to the right ")
    print("changes and an old rusty lever emerges. You are now so close")
    print("but you hesitate, is continuing really the right option?") 
    print("---------------------------------------")
    print("What will be your choice? (1 or 2)")
    print("-- 1 -- Pull the lever")
    print("-- 2 -- Back away and head home")
    print("---------------------------------------")

    # Validation input
    answer = input("").lower().strip()
    while answer not in "1" and answer not in "2":
        print("You have to make a choice, please try again")
        answer = input("").lower().strip()
        continue
    if answer == "1":
        clear_terminal()
        print("---------------------------------------")
        print("Good choice, let's finally find out the truth!")
        print("---------------------------------------")
        hiddenroom()
    elif answer == "2":
        clear_terminal()
        print("---------------------------------------")
        print("Well not every one can be the brave one.. ")
        print("---------------------------------------")
        game_over()


def hiddenroom():
    """
    """
    clear_terminal()
    print("You hear a click when pulling down the lever and the wall")
    print("inside the fireplace disappears. You decide that it's now or")
    print("never and head inside! ")
    print("After removing some cobwebs you turn on the flashlight and ")
    print("start looking around, you stop when you see a picture of ")
    print("your great-grandparents hanging above the chest.")
    print("The light of your flashlight reveals an inscription ")
    print("below the picture, so the family legend was true?!")
    print()
    print(" -- When the planets are aligned an important choice will ")
    print("be clear. Always remember, blood is thicker than water. --")
    print()
    print("You brush off the dust on the chest and two keyholes are revealed ")
    print("with two images above. The one to the left displays a heart ")
    print("that are being pierced by two daggers, the one to the right")
    print("shows a blowing leaf with a crown attached to the stem.")
    print("---------------------------------------")
    print(f"Which one could lead to the {lname} treasure? (1 or 2)")
    print("-- 1 -- The blowing leaf")
    print("-- 2 -- The heart")
    print("---------------------------------------")

    # Validation input
    answer = input("").lower().strip()
    while answer not in "1" and answer not in "2":
        print("You have to make a choice, please try again")
        answer = input("").lower().strip()
        continue
    if answer == "1":
        clear_terminal()
        print("---------------------------------------")
        treasure()
    elif answer == "2":
        clear_terminal()
        print("---------------------------------------")
        spirits()


def treasure():
    """
    """
    clear_terminal()
    print("You decide to go with the blowing leaf and to your")
    print("excitement you open the chest and finds it containing")
    print("more gold than you have ever seen. As you start to fill")
    print("your pockets with the gold you see a red light beaming")
    print("from the lid. You have no time to think before you get")
    print("sucked inside the chest and all is black")
    print("---------------------------------------")
    game_over()


def spirits():
    """
    """
    clear_terminal()
    print("You decide to go with the heart pierced with two daggers ")
    print("and as you turn around the key you find the chest eampty. ")
    print()
    print("You try to hide your disapointment and are about to leave ")
    print("when you see a blue light beam from the lid. You have ")
    print("managed to free the souls of your grandparents, a warm ")
    print("feeling replaces the coldness you felt before. Finally the curse")
    print(f"of the - {lname} family - is over!")
    print("---------------------------------------")
    game_over()


play_game()
