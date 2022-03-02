"""
By useing this class we can creat an object that will let us use the object
as a real dice. The object will have tow variables that will be used to control the roll
made and the sum of the all roll made.

you can easily roll a dice by using the function:

    roll()
    
"""

import random

class Dice():

    """
    Dice class that will allow us to make an instances of a reall dice.
    """
    intro = "PIG GAME.\n"
    

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


