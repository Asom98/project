"""unittest"""

import unittest
import diceHand

class testDiceHandClass(unittest.TestCase):
    """testing the dice_hand class"""

    def test_init_default_object(self):
        """Testing with the appropriate assert functions if the object is instance of dice_hand class"""

        #Making an abject of dice_hand class
        dicehand_object = diceHand.DiceHand() 
        self.asserIsInstance(dicehand_object, diceHand.DiceHand)

    
    def test_add_dice(self):
        """testing if we could add a dice to the dice_hand list"""

        dicehand_object = diceHand.DiceHand()
        dicehand_object.add_dice(1)

        exp = dicehand_object.dice_hand.count()

        self.assertEqual(exp, 1)


    def test_Show_dice_hand(self):
        """testing if we could get all the values inside the list"""

        dicehand_object = diceHand.DiceHand()
        dicehand_object.add_dice(1)

        exp = dicehand_object[0] == 1

        self.assertTrue(exp)

    
    def test_sum(self):
        """testing if we could get the sum of values inside the list"""

        dicehand_object = diceHand.DiceHand()
        dicehand_object.add_dice(1)
        dicehand_object.add_dice(1)

        exp = 2

        self.assertEqual(exp, dicehand_object.sum())

    
if __name__ == '__main__':
    unittest.main()

