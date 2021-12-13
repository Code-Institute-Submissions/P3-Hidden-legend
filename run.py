# developer: Madelene Eriksson
# description: Text-based mystery adventure game
# Name:

# Write your code to expect a terminal of 80 characters wide and 24 rows high

import time


def play_game():
    """
    This function is called when you start up the game.
    Works like a homepage. This function works on a
    global scale.
    """

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
    print("find the truth? (1 or 2)")
    print()
    print("1.) Hell yeah!")
    print("2.) No to much preasure..")

    answer = input("").lower().strip()
    while answer not in 1 and answer not in 2:
        print("You have to make a choice, please try again")
        answer = input("").lower().strip()
    if answer in 1:
        print("Such a good answer, there is no time like the present!")
        global fname
        fname = input("What is your first name? \n")
        global lname
        lname = input("What is your last name? \n")


play_game()


def introduction():
    """
    Introducing a storyline for the player where they have the,
    opportunity to chose to embark on the adventure
    """
    print("\nGrowing up you never knew much about your family history")
    print("and that was why you were surprised to find a suspicious")
    print("envelope in the mail a couple of weeks ago.")
    print("The information inside it didn't make sense for you")
    print("but the thing that you couldn't shake from your mind")
    print("was the the picture drawn at the bottom of the page.")
    print("It was a family chest with a heart pierced by two daggers. ")
    print()
    print("You took a look at the envelope again, still confused with why")
    print("this was sent to you. With frustration you threw the piece of")
    print("paper into the fire and a watermark became visible! You began")
    print("to try to rescue the paper from the fire and while looking at")
    print("it you saw an adress. The plot thickens, should you go? ")
    print()
    print("1.) No time to loose lets go!")
    print("2.) This adventure is not meant for me..")
    print()


def choicepresented():
    choice = ""
    while choice != "1" and choice != "2":
        choice = input("which choice will you make? (1 or 2): ")

    return choice


introduction()
choicepresented()


def start():
    """
    Gives the player their first choice which will affect their journey
    """
    print("\n The legend about this house has been passed down for")
    print("generations.")
    print("The legend about the family chest that is hidden somewhere")
    print("inside the  has long been a subject for")
    print("discussion in the [lname] household.")
    print("")


def greenhouse():
    """
    """
    print("You navigate your way inside the greenhouse,")
    print("avoiding all the debris laying on the ground.")
    print("[fname] starts to move the flashlight up and down")
    print("and notice a spiral staircase hidden in the corner.")
    print("It is old and rusty and have a specific pattern ")
    print("engraved in the steel that reminds you of stars and moons")
    print("Suddenly you hear a sound behind you and when you start ")
    print("to turn around you see something move next to the fountain.")
    print("You can either continue and make your way to the staircase or")
    print(" investigate what moved next to the fountain.")
    print("What will be your choice? (1 or 2)")
    print("1.) Staircase")
    print("2.) Fountain")


def fountain():
    """
    """
    print("You take a couple of steps forward with the heart pumping")
    print("in your chest. The sound came from underneath a large box")
    print("placed next to the fountain, after taking a deep breath")
    print(" you decide to kick the box and a rat trapped underneath")
    print("makes you jump. When you calm down you see some types of symbols")
    print("engraved in the stone. Next to it you find a strange looking key.")
    print("After taking the key you take a look on the symbols on the ground.")
    print("You remove the mosss and you suddenly see something")
    print("resembeling a bookcase and the different moon phases.")
    print("You realise that it is something meant to be found inside")
    print("this house.")
    print()
    print("You decide that the symbols could mean two places (1 or 2)")
    print("1.) Head to the staircase")
    print("2.) Move on to the library")


def library():
    """
    """
    print("\nAfter taking your first steps inside the library you feel")
    print("a cold chill moving down your spine and you know instantly")
    print("that you are on the right place. You try to flip a switch")
    print("and to your relief a dim light turns on and you move towards")
    print("the bookcase. When you starting to scan the titles you see an")
    print("anstronomy book an your curiosity takes over. When you start")
    print("pulling the book out the picutre to the right changes and a")
    print("old rusty lever emerges. You are now so close but you hesitate,")
    print("is continuing really the right option? ")
    print()
    print("1.) Pull the lever")
    print("2.) Back away and head home")


def hiddenroom():
    """
    """
    print("You hear a click when pulling down the lever and the wall")
    print("inside the fireplace disappear. You decide that it's now or")
    print("never and head inside! ")
    print("After removing some cobwebs you turn on the flashlight and ")
    print("start looking around, you stop when you see a picture of ")
    print("your great-grandparents hanging above the chest.")
    print("The light of your flashlight reveals a inscription ")
    print("below the picture, so the family legend was true!?")
    print(" -- When the planets are in alignment an important choice will ")
    print("be clear. Always remember, blood is thicker than water. --")
    print("You brush of the dust on the chest and two keyholes is revealed ")
    print("with two images above. The one to the left displays a heart ")
    print("that are being pierced by two daggers, the one to the right")
    print("shows a blowing leaf with a crown attached to the stem.")
    print()
    print("Which one could lead to the [lname] treasure?")
    print("1.) The blowing leaf")
    print("2.) The heart")


def treasure():
    """
    """
    print("You decide to go with the blowing leaf and to your ")
    print("excitement you open the chest and finds it containing")
    print("more gold then you ever seen. As you start to fill ")
    print("your pockets with the gold you see a red light beaming")
    print("from the lid. You have no time to think before you get")
    print("sucked inside the chest and all is black")


def spirits():
    """
    """
    print("You decide to go with the heart piercied with two daggers ")
    print("and as you turn around the key you find the chest eampty. ")
    print("You try to hide your disapointment and are about to leave ")
    print("when you see a blue light beam from the lid. You have ")
    print("manages to free the souls of your grandparents, a warm ")
    print("feeling replaces the cold you had before. Finally the curse")
    print("is over!")


print("\n Hi")
