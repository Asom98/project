"""

This is going to be the game file(class) where all the funktions are executed

in the main function, those funktions will be imported from the other classes in the same package

that will build the pig game!.

"""

import player


def main():
    
    information()


    


def information():
    """In this function will all the information needed to play the game be printed"""

    print("======================== Pig ========================")
    print("=============== Wellcome to pig game! ===============")
    print("")
    print("You will be provided with all the informations to play the game.")
    print("The game consist of either tow players or you can play with an AI(computer).")
    print("you will be able to choose a name and change it later(chooseable!).")
    print("The object of the game to be the first player to reach 100 points, and ")
    print("the points are scored by rolling a dice 1-6 and avoid rolling a 1.")
    print("Players can roll as many as they want but if they get a 1 the points ")
    print("sets to 0, the player chooses to stop rolling and gather the points and so on.")
    print("Be carefull getting a 1 will erase all the points that you have!")
    print("The score will be tracked and the first player to reache 100 point will win.")
    print("")
    print("======================= Enjoy =======================")

    



if __name__ == '__main__':
    # Calling the main function to execute the game.
    main()