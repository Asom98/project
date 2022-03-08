"""Unittest"""

import unittest
import player


class testPlayerClass(unittest.TestCase):
    """Testing the Player class"""

    def test_init_default_object(self):
        #Making an abject of player class with the name Mike
        player_object = player.Player("Mike")

        #Testing with the appropriate assert functions
        #  if the object is instance of player class
        self.assertIsInstance(player_object, player.Player)

    
    def test_change_name(self):
        #Making an abject of player class with the name Mike
        player_object = player.Player("Mike")
        
        #Creating seconed name to be changed to
        sec_name = "Andy"
        player_object.change_name(sec_name)
        self.assertEqual(player_object.get_name(), sec_name)


if __name__ == '__main__':
    unittest.main()


    


