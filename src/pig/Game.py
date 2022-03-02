"""

This is going to be the game file(class) where all the funktions are executed

in the main function, those funktions will be imported from the other classes in the same package

that will build the pig game!.

"""

import player
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

    player2 = player.Player("Stina")
    print(player2.get_name())

    player3 = player.Player("Simon")
    print(player3.get_name())

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