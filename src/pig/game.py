"""

This is going to be the game file where all the funktions are executed

in the main function, those functions will be imported from the other classes in the same package

that will build the pig game!.


"""

import dice
import diceHand
import intelligence
import player


def main():


    points_to_win = 25

    set_name = True
    game_on = True

    information()
    

    mode = game_mode() #choosing the game mode

    while game_on:

        while(mode == 1):  #player against AI
            
            while(set_name):

                print("Player against AI")
                name = input("First player! Set your name here >> ")
                print        ("==================================")
                print("")
                print("==================================")
                print("")

                dice1 = dice.Dice()
                player1 = player.Player(name)                
                diceHand1 = diceHand.DiceHand()
                diceHand2 = diceHand.DiceHand()
                
                #set game difficulty
                difficulty = int(input("Choose your desired difficulty level. \nPress (1) for normal. \nPress (2) for hard."))
                computer = intelligence.Intelligence()



                print("")
                print("==================================")
                print("")
                    
                    
                

                set_name = False

            while difficulty == 1:
                computer.normal_difficulty()
                want_roll = True

                while (want_roll):
                    print('(', player1.get_name(),')', "turn to roll a dice: ")
                    value1 = dice1.roll()
                    print("You rolled: " , value1)

                    if value1 == 1:

                        diceHand1.add_dice(value1)
                        print("OBS! you have rolled a 1. All your points will be erased!")
                        print("and it will be your opponent turn.")
                        print(diceHand1.show_dice_hand())
                        print("here is your sum points: ", diceHand1.sum())
                        
                        print("")
                        print("==================================")
                        print("")
                        
                        want_roll = False
                    else:
                        diceHand1.add_dice(value1)
                        print("here is your current dices")
                        print(diceHand1.show_dice_hand())
                        print("here is your sum points: ", diceHand1.sum())
                        if diceHand1.sum() >= points_to_win:
                            print("Congrats! ", player1.get_name(), "won the game.")
                            print("")
                            print("==================================")
                            print("")
                            mode = 0
                            difficulty = 0
                            want_roll = False
                            break

                        answer = input("Do you want to roll agin? y/yes, n/no, c/change name, $/to cheat >> ")
                        print("")
                        print("==================================")
                        print("")
                        if answer == "y":
                            continue
                        elif answer == "c":
                            new_name = input("Enter a new name please >> ")
                            player1.change_name(new_name)
                        elif answer == "$":
                            diceHand1.add_dice(10)
                        else:
                            want_roll = False
                            print("")
                            print("==================================")
                            print("")

                if mode == 1:
                    want_roll = True
                else:
                    want_roll = False
                
                while (want_roll):

                    print("Computer turn to roll a dice: ")
                    value2 = dice1.roll()
                    print("Computer rolled: " , value2)

                    if value2 == 1:
                        print("OBS! computer have rolled a 1. All computer points will be erased!")
                        print("and it will be player's turn.")
                        diceHand2.add_dice(value2)
                        print("here is computer's current dices")
                        print(diceHand2.show_dice_hand())
                        print("here is computer's sum points: ", diceHand2.sum())
                        print("")
                        print("==================================")
                        print("")
                        want_roll = False
                    else:
                        diceHand2.add_dice(value2)
                        print("here is computer's current dices")
                        print(diceHand2.show_dice_hand())
                        print("here is computer's sum points: ", diceHand2.sum())
                        print("")
                        print("==================================")
                        print("")
                        if diceHand2.sum() >= points_to_win:
                            print("Computer won the game.")
                            print("")
                            print("==================================")
                            print("")
                            mode = 0
                            difficulty = 0
                            want_roll = False
                            break
                
            while difficulty == 2:
                computer.hard_difficulty()
                want_roll = True

                while (want_roll):
                    print('(', player1.get_name(),')', "turn to roll a dice: ")
                    value1 = dice1.roll()
                    print("You rolled: " , value1)

                    if value1 == 1:

                        diceHand1.add_dice(value1)
                        print("OBS! you have rolled a 1. All your points will be erased!")
                        print("and it will be your opponent turn.")
                        print(diceHand1.show_dice_hand())
                        print("here is your sum points: ", diceHand1.sum())
                        
                        print("")
                        print("==================================")
                        print("")
                        
                        want_roll = False
                    else:
                        diceHand1.add_dice(value1)
                        print("here is your current dices")
                        print(diceHand1.show_dice_hand())
                        print("here is your sum points: ", diceHand1.sum())
                        if diceHand1.sum() >= points_to_win:
                            print("Congrats! ", player1.get_name(), "won the game.")
                            print("")
                            print("==================================")
                            print("")
                            mode = 0
                            difficulty = 0
                            want_roll = False
                            break

                        answer = input("Do you want to roll agin? y/yes, n/no, c/change name, $/to cheat >> ")
                        print("")
                        print("==================================")
                        print("")
                        if answer == "y":
                            continue
                        elif answer == "c":
                            new_name = input("Enter a new name please >> ")
                            player1.change_name(new_name)
                        elif answer == "$":
                            diceHand1.add_dice(10)
                        else:
                            want_roll = False
                            print("")
                            print("==================================")
                            print("")

                if mode == 1:
                    want_roll = True
                else:
                    want_roll = False
                
                while (want_roll):

                    print("Computer turn to roll a dice: ")
                    value2 = computer.hard_roll()
                    print("Computer rolled: " , value2)

                    if value2 == 1:
                        print("OBS! computer have rolled a 1. All computer points will be erased!")
                        print("and it will be player's turn.")
                        diceHand2.add_dice(value2)
                        print("here is computer's current dices")
                        print(diceHand2.show_dice_hand())
                        print("here is computer's sum points: ", diceHand2.sum())
                        print("")
                        print("==================================")
                        print("")
                        want_roll = False
                    else:
                        diceHand2.add_dice(value2)
                        print("here is computer's current dices")
                        print(diceHand2.show_dice_hand())
                        print("here is computer's sum points: ", diceHand2.sum())
                        print("")
                        print("==================================")
                        print("")
                        if diceHand2.sum() >= points_to_win:
                            print("Computer won the game.")
                            print("")
                            print("==================================")
                            print("")
                            mode = 0
                            difficulty = 0
                            want_roll = False
                            break


        while(mode == 2):  #palyer vs another
            print("Player against Player")
            
            while(set_name):
                name1 = input("First player! Set your name here >> ")
                name2 = input("Second player! Set your name here >> ")
                print        ("==================================")
                print("")
                print("==================================")
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

                    diceHand1.add_dice(value1)
                    print("OBS! you have rolled a 1. All your points will be erased!")
                    print("and it will be your opponent turn.")
                    print(diceHand1.show_dice_hand())
                    print("here is your sum points: ", diceHand1.sum())
                    
                    print("")
                    print("==================================")
                    print("")
                    
                    want_roll = False
                else:
                    diceHand1.add_dice(value1)
                    print("here is your current dices")
                    print(diceHand1.show_dice_hand())
                    print("here is your sum points: ", diceHand1.sum())
                    if diceHand1.sum() >= points_to_win:
                        print("Congrats! ", player1.get_name(), "won the game.")
                        print("")
                        print("==================================")
                        print("")
                        mode = 0
                        want_roll = False
                        break

                    answer = input("Do you want to roll agin? y/yes, n/no, c/change name, $/to cheat >> ")
                    print("")
                    print("==================================")
                    print("")
                    if answer == "y":
                        continue
                    elif answer == "c":
                        new_name = input("Enter a new name please >> ")
                        player1.change_name(new_name)
                    elif answer == "$":
                        diceHand1.add_dice(10)
                    else:
                        want_roll = False
                        print("")
                        print("==================================")
                        print("")

            if mode == 2:
                want_roll = True
            else:
                want_roll = False

            while (want_roll):

                print('(', player2.get_name(),')', "turn to roll a dice: ")
                value2 = dice1.roll()
                print("You rolled: " , value2)

                if value2 == 1:
                    print("OBS! you have rolled a 1. All your points will be erased!")
                    print("and it will be your opponent turn.")
                    diceHand2.add_dice(value2)
                    print("here is your current dices")
                    print(diceHand2.show_dice_hand())
                    print("here is your sum points: ", diceHand2.sum())
                    print("")
                    print("==================================")
                    print("")
                    want_roll = False
                else:
                    diceHand2.add_dice(value2)
                    print("here is your current dices")
                    print(diceHand2.show_dice_hand())
                    print("here is your sum points: ", diceHand2.sum())
                    if diceHand2.sum() >= points_to_win:
                        print("Congrats! ", player2.get_name(), "won the game.")
                        print("")
                        print("==================================")
                        print("")
                        mode = 0
                        want_roll = False
                        break

                    answer = input("Do you want to roll agin? y/yes, n/no, c/change name, $/to cheat >> ")
                    print("")
                    print("==================================")
                    print("")
                    if answer == "y":
                        continue
                    elif answer == "c":
                        new_name = input("Enter a new name please >> ")
                        player2.change_name(new_name)
                    elif answer == "$":
                        diceHand2.add_dice(10)
                    else:
                        want_roll = False
                        print("")
                        print("==================================")
                        print("")

        answer1 = input("Do you want to play again? y/yes, n/no >> ")
        if answer1 == "y":
            mode = game_mode() 
            set_name = True
        else:
            print("See you again! thanks for playing.")
            game_on = False


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
    print("Read the information above to understand the game!")
    print("If you want to play alone press (1). ")
    print("If you want to play versus another player press (2).")
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


if __name__ == '__main__':
    # Calling the main function to execute the game.
    main()