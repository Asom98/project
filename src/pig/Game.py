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

    



if __name__ == '__main__':
    # Calling the main function to execute the game.
    main()