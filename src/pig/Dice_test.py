"""Unit testing"""

import unittest
import dice

class testDiceClass():
    """Testing the dice class"""

    def test_init_default_object(self):
        #Making an abject of Dice class
        dice_object = dice.Dice()

        #Testing with the appropriate assert functions
        #  if the object is instance of Dice class
        self.assertIsInstance(dice_object, dice.Dice)

    
    def test_faces(self):
        #Making an abject of Dice class
        dice_object = dice.Dice()

        #Testing if the dice object has right number of faces
        self.assertEqual(dice_object.faces, 6)


    def test_roll_dice(self):
        #Making an abject of Dice class
        dice_object = dice.Dice()

        #Testing if the rolled face is between 1-6
        res = dice_object.roll()
        exp = 1 <= res <= dice_object.faces
        self.assertTrue(exp)


if __name__ == '__main__':
    unittest.main()  

