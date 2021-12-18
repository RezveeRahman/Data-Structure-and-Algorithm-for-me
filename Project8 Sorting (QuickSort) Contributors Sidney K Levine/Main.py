#Sidney K Levine, Rezvee Rahman
#CSC212-03
#Quick Sort Algorithm

#Imports
from typing import List
import QuickSort
import readFile
import time

def main():
    print("Initializing Quick Sort Algorithm.\n")

    while True:
        try:
            print("\t1-Start\n\t2-Exit")
            choice = int(input("Please enter an input corresponding with the menu choices: "))

            if(choice == 1):
                print("Initializing code implemetentation.\n")
                S_time = time.time()
                List = readFile.lineReturner(readFile.readfile_())

                QuickSort.QuickSort(List,0, len(List)-1)

                print(List)
                F_time = time.time()

                print('{time:.2f} time'.format(time = F_time-S_time))
            elif(choice == 2):
                print("Exiting")
                break
            else:
                print("Enter a value corresponding withthe menu choices.\n")
        except ValueError:
            print("Enter a integer value")



if __name__ == "__main__":
    main()