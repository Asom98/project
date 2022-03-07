"""
This class create an object that will function as a real dice. 
The object will have two variables that will be used to control the rolls
made by the players and the sum of the all rolls that was made.

By rolling the dice this function is used:

    roll()
    
"""

import random

class Dice():

    """
    Dice class that will allow us to make an instances of a reall dice.
    """


    def __init__(self):

        """Roll a dice once and return the value."""
        #random.seed()
        # these variables will be different for each instance
        self.roll_made = 0
        self.sum_of_rolls = 0



    def roll(self):

        """Roll a dice and return result face value"""
        self.roll_made +=1
        #Making random number between 1-6 and adding the value
        roll = random.randint(1,6)
        self.sum_of_rolls += roll

        return roll


