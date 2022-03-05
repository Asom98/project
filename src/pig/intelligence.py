"""This class is used if the player picks gamemode (1). 
It should roll the dice by itself.
It should have 2 difficulty levels, one normal and one hard.

Add AI decision making, if there is time. 
Ex. if the computer manages to collect enough points, it should stop rolling.

Possibility of having the harder difficulty AI be more risk-averse.
Stopping it's turn faster than it's normal counterpart.

"""

class Intelligence():

    # AI always has the same name

    def __init__(self):
        pass


    # General behavior
    def action(self, roll):
        print(f"Computer rolls a: {roll}")


    # Behavior for normal difficulty AI
    def normal_difficulty(self):
        print("You have picked 'normal' difficulty!")
        
        

    # Behavior for hard difficulty AI
    def hard_difficulty(self):
        print("You have picked 'hard' difficulty!")
        
        




