import random

class Dice():

    """
    Dice class that will allow us to make an instances of a reall dice.
    """

    # variable that all the instances of the dice class will have
    faces = 6

    def __init__(self):

        """Roll a dice once and return the value."""
        random.seed()
        # these variables will be different for each instance
        self.roll_made = 0
        self.sum_of_rolls = 0

    '''
    def set_faces(self, faces):

        """Determine how many faces to set on the dice"""
        self.faces = faces
        print(f"The faces of the dice are now: {self.faces}")
    '''


    def roll(self):

        """Roll a dice and return result face value"""
        self.roll_made +=1
        #Making random number between 1-6 and adding the value
        roll = random.randint(1,6)
        self.sum_of_rolls += roll
        return roll


