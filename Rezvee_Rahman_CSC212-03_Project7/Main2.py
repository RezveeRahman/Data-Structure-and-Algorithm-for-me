#Rezvee Rahman
#CSC212-03
#Linked List Project 7

#imports
import LinkedList
import Openfile



def main():
    print("Organizer linked list\n")
    while True:
        

        try:
            #Choices menu
            print("\t1 - Linked List \n\t2 - Exit")
            choice = int(input("Please enter the value corresponding with the menu choices: "))


            if(choice == 1):
                    #Ask for the filename, if not found then we should break from the code
                    F_name = input("Enter the file name to get the list from with extension: ")
                    storedVal = Openfile._readfilevalues(Openfile._openfile_read(F_name))

                    if(storedVal == None):
                        print("Returning to the main menu.")
                    else:
                        #Create an unordered list for now. 
                        #Ordered list will come later on in Version 2
                        Olinkedlis = LinkedList.OrLi()

                        for i in storedVal:
                            if(i[0] == 'insert'):
                                Olinkedlis._append(i[1])
                                print("Adding to linkedlist the {},The current size of the linked list is {}.\n".format(i[1],Olinkedlis.size()))
                            elif(i[0] == 'delete'):
                                Olinkedlis.remove(i[1])
                                print("Removing from the list {}, The current size of the linked list is {}\n".format(i[1],Olinkedlis.size()))
                            else:
                                print("Can't parse information, skipping.")
                            
                            Olinkedlis._getLink()

                            input("\nPress enter to continue")


            elif(choice == 2):
                print("Exiting.\n")
                break
            else:
                print("Makesure you enter a value coressponding with the menu options.\n")
        
        except ValueError:
            print("Could not parse please enter a integer value")



if __name__ == "__main__":
    main()