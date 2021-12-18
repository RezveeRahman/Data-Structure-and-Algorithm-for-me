#Name: Rezvee Rahman
#Class: CSC212-03
#Project 1: State Guessing Game

#IMPORTS
#==========================
import pickleModule as pM
import Guesser as Guess
#==========================
def main():
    Ended = False
    print("Welcome to guesser game (by Rezvee Rahman) Please take a look at the choices")
    while not Ended:
        print("1 - Start new Game\n2 - Convert random questions and answers\n3 - exit")
        try:
            response_menu = int(input("Please enter the number for the corresponding choices: "))

            if(response_menu == 1):
                print("Initializing New game")
                Guess.guesser(pM.unpickle_data(pM.openFileRB()))
                print("\nReturning to Main Menu")
            elif(response_menu == 2):
                print("Please Note this will overwrite the existing .dat file. To prevent this enter an unknown file.")
                pM.filepickling(pM.fileConversionDict(pM.openFileR()))
            elif(response_menu == 3):
                Ended = True
                print("\nExiting")
                break
            else:
                print("Invalid Option choice.")
        except ValueError:
            print("Please use whole integers")
        except ModuleNotFoundError:
            print("Modules could not be found! Critical error! Files are corrupted. Please check the README.txt for help.")
            break

    pass

if __name__=='__main__':
    main()

