"""Unittest"""

import unittest
import player


class testPlayerClass():
    """Testing the Player class"""

    def test_init_default_object(self):
        #Making an abject of player class
        player_object = player.Player("Mike")

        #Testing with the appropriate assert functions
        #  if the object is instance of player class
        self.asserIsInstance(player_object, player.Player)

    
    def test_change_name(self):
        """testing to change the name"""

        player_object = player.Player("Mike")
        exc = "kalle"

        player_object.change_name(exc)

        self.assertEqua(exc, player_object.get_name())


        

    


