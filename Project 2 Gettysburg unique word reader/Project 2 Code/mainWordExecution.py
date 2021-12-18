#Rezvee Rahman
#Class: CSC212-03
#Project 2 Word Counter

#imports
import lineReader

#Main function
def main():
    while True:
        print("Please enter a number for the following choices.\n")
        print("1- for reading the unique words\n2- for exiting the program.")
        try:
            choice = int(input("Entry: "))
            if(choice==1):
                lineReader.count_words_unique(lineReader.line_read(lineReader.readSelectFile()))
                print("Successful")
            elif(choice==2):
                print("Exiting")
                break
            else:
                print("Try to enter a legit value.")
        except ValueError:
            print("Please enter a from the menu choices.\n")

main()
