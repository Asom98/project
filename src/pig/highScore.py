"""keep track of highscore of the players"""

class HighScore:

    HighScore = 0

    def serach_for_high(self,first_list, sec_list):
        var1 = 0
        var2 = 0

        for x in first_list:

            var1 += x
            

        for y in sec_list:
            
            var2 += y
            

        if var1 > var2:
            
            self.HighScore = var1
           #print("dice hand 1")
            return self.HighScore
        else:

            self.HighScore = var2
            #print("dice hand 2")
            return self.HighScore 

        


        