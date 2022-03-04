"""

This is going to be the game file where all the funktions are executed

in the main function, those functions will be imported from the other classes in the same package

that will build the pig game!.


"""

import dice
import diceHand
import player
import highScore


def main():

    set_name = True

    information()

    mode = game_mode() #choosing the game mode

    while(mode == 1):  #player against AI
        print("Player against AI")
        break

    while(mode == 2):  #palyer vs another
        while(set_name):
            
            name1 = input("First player! Set your name here >> ")
            name2 = input("Second player! Set your name here >> ")
            print        ("==================================")
            print("")
            print("=========================================================")
            print("")

            dice1 = dice.Dice()

            player1 = player.Player(name1)
            player2 = player.Player(name2)

            diceHand1 = diceHand.DiceHand()
            diceHand2 = diceHand.DiceHand()
    
            set_name = False

        
        want_roll = True

        while (want_roll):
            print('(', player1.get_name(),')', "turn to roll a dice: ")
            value1 = dice1.roll()
            print("You rolled: " , value1)

            if value1 == 1:
<<<<<<< HEAD

                print("OBS! you have rolled a 1. All your points will be erased!")
                print("and it will be your opponent turn.")
                print("")
                print("=========================================================")
                print("")
=======
                print("OBS! You have rolled a 1. All your points will be erased!")
                print("It is now your opponent's turn.")
                print("|")
                print("|")
>>>>>>> 62a6db304ac82b157de00ca76a568f37c2c9dcde
                diceHand1.add_dice(value1)
                want_roll = False
            else:
                diceHand1.add_dice(value1)
                answer = input("Do you want to roll agin? y/yes, n/no >> ")
<<<<<<< HEAD
                print("")
                print("=========================================================")
                print("")
=======
                print("|")
                print("|")

>>>>>>> 62a6db304ac82b157de00ca76a568f37c2c9dcde
                if answer == "y":
                    continue
                else:
                    want_roll = False
                    print("")
                    print("=========================================================")
                    print("")
        
        want_roll = True

        while (want_roll):

            print('(', player2.get_name(),')', "turn to roll a dice: ")
            value2 = dice1.roll()
            print("You rolled: " , value2)

            if value2 == 1:
                print("OBS! you have rolled a 1. All your points will be erased!")
                print("and it will be your opponent turn.")
                print("")
                print("=========================================================")
                print("")
                diceHand2.add_dice(value2)
                want_roll = False
            else:
                diceHand2.add_dice(value2)
                answer = input("Do you want to roll agin? y/yes, n/no >> ")
                print("")
                print("=========================================================")
                print("")
                if answer == "y":
                    continue
                else:
                    want_roll = False
                    print("")
                    print("=========================================================")
                    print("")



def information():
    """In this function will all the information needed to play the game be printed"""

    print("===================== Pig game ======================")
    print("=============== Welcome to pig game! ===============")
    print("")
    print("You will be provided with all the information needed to play the game.")
    print("The game consists of either two players, or you can play with an AI(computer).")
    print("You will be able to choose a name and change it later(chooseable!).")
    print("The object of the game is to be the first player to reach 100 points. ")
    print("The points are scored by rolling a dice 1-6 and avoid rolling a 1.")
    print("Players can roll as many times as they want, but if they roll a 1 the points ")
    print("of your current turn gets set to 0. The player can choose to stop rolling and gather the points at any time.")
    print("The score will be tracked and the first player to reach 100 points will win.")
    print("")
    print("======================= Enjoy =======================")
    print("")



def game_mode():
    """Here the player will choose to play with an AI or another player"""

    #the func will return 1 or 2 which determines the game mode
    print("If you want to play alone press (1). If you want to play versus another player press (2): ")
    print("")




    try:
        choice = int(input("Please enter 1 or 2 >> "))
    except ValueError:
        print("You have entered an invalid value. Try again!")
    except TypeError:
        print("You have entered an invalid value. Try again!")
    except:
        print("You have entered an invalid value. Try again!")
        

    while choice > 2 or choice <= 0:
         choice = int(input("Please enter 1 or 2 >> "))

    return choice


def play_turn():
    # A player rolls the die and gets a score
    player_bob = player.Player('Bob')
    score = 3

    # Set player's score
    player_bob.current_score = score

def end_game():
    player_bob = player.Player('Bob')

    # Set player's highscore
    if player_bob.score > player_bob.highscore:
        player_bob.highscore = player_bob.score


"""
    # Write player to file at the end of the game
    with open('players/Bob.pkl', 'wb') as f:
        pickle.dump(f, player_bob)
"""


if __name__ == '__main__':
    # Calling the main function to execute the game.
    main()