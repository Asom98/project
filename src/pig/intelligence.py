"""
This class is used if the player picks gamemode (1). 
It should roll the dice by itself.
It should have 2 difficulty levels, one normal and one hard.

Add AI decision making, if there is time. 
Ex. if the computer manages to collect enough points, it should stop rolling.

Possibility of having the harder difficulty AI be more risk-averse.
Stopping it's turn faster than it's normal counterpart.
"""
import random
import dice


class Intelligence():

    def __init__(self):
        # name can be 'Computer (Normal) or Computer (Hard)
        pass
    

    # Behavior for normal difficulty AI
    def normal_difficulty(self):
        """Picking this option sets ai name to 'Computer (Normal)"""
        """This difficulty has the same rolling behaviour as player"""

        print("You have picked 'normal' difficulty!")
        
                

    # Behavior for hard difficulty AI
    def hard_difficulty(self):
        """Picking this option sets ai name to 'Computer (Hard)"""
        """This difficulty is almost impossible to beat. It can only roll a 5 or 6"""

        print("You have picked 'hard' difficulty!")
        
    
    
    def hard_roll(self):
        """Roll a dice and return result face value"""
        
        #Making random number between 4-6 and adding the value to be hard for the player
        list = [1,5,5,6]
        roll = random.choice(list)
        
        return roll
    