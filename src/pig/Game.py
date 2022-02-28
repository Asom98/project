"""

This is going to be the game file(class) where all the funktions are executed

in the main function, those funktions will be imported from the other classes in the same package

that will build the pig game!.

"""

import player


def main():

    player1 = player.Player("Stina")
    print(player1.get_name())

    player2 = player.Player("Stina")
    print(player2.get_name())

    player3 = player.Player("kalle")
    print(player3.get_name())



if __name__ == '__main__':
    # Calling the main function to execute the game.
    main()