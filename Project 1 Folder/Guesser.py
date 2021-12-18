#Rezvee Rahman
#Guesser Section

import math
import random
from typing import List
import pickleModule

#Will take a set and randomly pick a value
def guesser(dictionary_dat):
    try:
        #Creating Key list
        Key_items = list(dictionary_dat.keys())

        #Loop to end the game for the current data file
        Ended_ = False
        while not Ended_:

            #From that list we pick a random value
            Rand_num = Key_items[random.randint(0,len(Key_items))]


            #Prompt user with the question
            print("What is the capital for the state{}?".format(Rand_num))
            for i in range(5):
                response = input("Enter your answer: ")
                if( dictionary_dat[Rand_num] == response):
                    print("Correct!")
                    break
                i+=1
                print("Incorrect! Try again ({} chances remaining)".format(5-i))
            print("\nThe correct answer is {} for{}".format(dictionary_dat[Rand_num],Rand_num))

            
            while True:
                try:
                    print("Would you like to try again?[type 'yes' to continue else 'no' to end]")
                    end_game = input("").lower()
                    if(end_game == "no"):
                        Ended_ = True
                        break
                    elif(end_game == "yes"):
                        Ended_ = False
                        break
                    else:
                        print("Try again")
                except ValueError:
                    print("Please print a valid selection.")

    except AttributeError:
        print("File has no attribute.")

#Creating a new game
#guesser(pickleModule.unpickle_data(pickleModule.openFileRB()))



    



    
