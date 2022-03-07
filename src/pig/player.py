"""
In this class the player instance will be made and

to be able to use it in the game.

Each player will have a name and will be able to change their name

when ever they want
"""

import unittest
import player

class Player():
    """Player class"""

        
    
    def __init__(self, name):
        """Make an instance of the player class"""
        #Name of the player
        self.name = name
    

    def change_name(self, name):
        """changing the name of the player"""
        self.name = name
        print(f"The name has been changed to: {self.name}")


    def get_name(self):
        """Getting the name of the player"""
        return self.name
    
    if __name__ == '__main__':
        unittest.main()


    
