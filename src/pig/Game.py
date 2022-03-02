"""

This is going to be the game file where all the funktions are executed

in the main function, those functions will be imported from the other classes in the same package

that will build the pig game!.

"""

import player
<<<<<<< HEAD
import pickle
import os



def main():

    player_name = 'Laura'

    # Check if serialized object for player with name
    # "Laura" exists
    if os.path.exists('players/' + player_name + '.pkl'):
        with open('players/' + player_name + '.pkl', 'rb') as f:
            # player_laura is an instance of Player
            player_laura = pickle.load(f)

    player1 = player.Player("Kassem")
    print(player1.get_name())
=======
import dice
import diceHand

def main():

    
    dice1 = dice.Dice()
    diceHand1 = diceHand.DiceHand()

    diceHand1.add_dice(dice1.roll())
    diceHand1.add_dice(dice1.roll())
    diceHand1.add_dice(dice1.roll())
    diceHand1.add_dice(dice1.roll())
    diceHand1.add_dice(dice1.roll())
    diceHand1.add_dice(dice1.roll())
    diceHand1.add_dice(dice1.roll())
    diceHand1.add_dice(dice1.roll())

    

    diceHand1.show_dice_hand()

    """
        information()

    mode = game_mode() #choosing the game mode

    while(mode == 1):  #player against AI
        print("player against AI")
        break

    while(mode == 2):  #palyer vs another
        print("palyer vs another")
        break
    """


    


def information():
    """In this function will all the information needed to play the game be printed"""

    print("===================== Pig game ======================")
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
    print("")



def game_mode():
    """Here the player will choose to play with an AI or another player"""

    #the func will return 1 or 2 which determines the game mode
    print("If you wanna play alone press (1). do you wanna play with another player press (2): ")
    print("")
    choice = int(input("please enter 1 or 2 >> "))

    while(choice > 2 or choice <= 0):
        
        choice = int(input("please enter 1 or 2 >> "))
    
    return choice
>>>>>>> f26441d98f996c5987a3e857402b3e7eaef098b2


<<<<<<< HEAD
    player3 = player.Player("Simon")
    print(player3.get_name())
=======
    
>>>>>>> f26441d98f996c5987a3e857402b3e7eaef098b2

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

    # Write player to file at the end of the game
    with open('players/Bob.pkl', 'wb') as f:
        pickle.dump(f, player_bob)

if __name__ == '__main__':
    # Calling the main function to execute the game.
    main()