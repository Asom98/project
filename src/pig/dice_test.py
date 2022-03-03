"""Unit testing"""

import unittest
import dice

class testDiceClass():
    """Testing the dice class"""

    def test_init_default_object(self):
        """Testing to make an object and check its properties"""

        #Making an abject of Dice class
        dice_object = dice.Dice()

        #Testing with the appropriate assert functions
        #  if the object is instance of Dice class
        self.assertIsInstance(dice_object, dice.Dice)

    
    def test_number_of_faces(self):
        """Testing that the dice has 6 faces"""
        #Making an abject of Dice class
        dice_object = dice.Dice()

        #Testing if the dice object has right number of faces
        self.assertEqual(dice_object.faces, 6)


    def test_roll_dice(self):
        """Testing that you can roll a dice and get from 1-6 from the rolled dice"""
        #Making an abject of Dice class
        dice_object = dice.Dice()

        #Testing if the rolled face is between 1-6
        res = dice_object.roll()
        exp = 1 <= res <= dice_object.faces
        self.assertTrue(exp)


if __name__ == '__main__':
    unittest.main()  

