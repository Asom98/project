
"""Unit testing high Score"""

# testing the function from the high score class to see which has the high score.

import unittest
import highScore

class testhighScore(unittest.TestCase): 
    def testForHighScore(self):
        var1 = [5,2,3]
        var2 = [3,4,5]

        # Making an object of the Highscore class
        highscore_object = highScore.HighScore()
        
        
        
        # Testing the function search_for_high from the highscore class
        self.assertEqual(highscore_object.serach_for_high(var2,var1),12)

if __name__ == '__main__':
    unittest.main()  