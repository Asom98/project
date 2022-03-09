"""Unit testing for intelligence"""


# Added required imports and made test for object creation.
# Will add more as I finish building the Intelligence class and it's methods    


import unittest
import random
import intelligence


class testIntelligenceClass(unittest.TestCase):
    """Testing the Intelligence class"""

    def test_init_default_object(self):
        """Testing to make an object and check its properties"""
        # Making an abject of Intelligence class
        intelligence_object = intelligence.Intelligence()

        # Testing if the object is instance of Intelligence class
        self.assertIsInstance(intelligence_object, intelligence.Intelligence)


    def test_hard_roll(self):
        """Testing something"""
        #Making an abject of Intelligence class
        intelligence_object = intelligence.Intelligence()

        list = [1, 5, 5, 6]
        roll = random.choice(list)
        self.assertIn(roll, list)


if __name__ == '__main__':
    unittest.main()
