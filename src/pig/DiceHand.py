"""
By using this class we can create an object where all the points are collected in to a list!
You can access the object by adding a value to thier list and showing all the
values in thier list.

Adding a value will happen easily by using:

    add_dice(dice_roll)

Showing all the values will happen when calling the following function:

    show_dice_hand()

"""


class DiceHand():
    """DiceHand class is used to save every value of the dice when it's rolled"""

    dice_hand = [] #list to save the values 


    def add_dice(self, dice_roll):
        """Here you will be able to add a rolled dice value to your dice hand"""

        #Adding the rolled dice value to dice_hand list
        if dice_roll == 1:

            self.dice_hand = []
        else:

            self.dice_hand.append(dice_roll)
        
        


    def show_dice_hand(self):
        """In this function you will go throw all the rolled dice you have made and be able to se them"""

        #loping throw the dice_hand list and see all the values  
        for x in self.dice_hand:
            print(x)

