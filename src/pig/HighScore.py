"""keep track of highscore of the players"""

def get_highscore():
    highscore = 0

    try:
        highscore_file = open("highscore_txt")
        highscore = int (highscore_file.read())
        print("High score:" , highscore)
        except IOError:
            print("error reading the file, there is no highscore")
            except ValueError:
                print("")
            return highscore

def save highscore(new_highscore)

        