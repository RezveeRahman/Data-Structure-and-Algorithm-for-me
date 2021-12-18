from Node import Node
from BST import BST

def main():
    print("Binary Search Tree make.\n")
    while True:
        print("Menu Choices: ")
        print("1 - Start Program\n2 - Exit")
        try:
            Choice = int(input("Enter your Choice [integer value]: "))
            if(Choice == 1):
                SearchTree = BST()
                print("What would you like to do?")
                while True:
                    print("1 - insert\n2 - Delete\n3 - Search\n4 - Traverse (PreOrder) \n5 - Traverse (InOrder) \n6 - Traverse (PostOrder) \n7 - Instructions to draw out Tree \n8 - Exit")
                    try:
                        Choice2 = int(input("Enter the following choices: "))
                        if(Choice2 == 1):
                            print("Inserting value to the BST")
                            try:
                                entry = int(input("Enter an Integer: "))
                                SearchTree.insert(entry)
                                input("Press [enter] to continue.\n")
                            except ValueError:
                                print("Please enter an integer Value (no float or decimal values). If you are trying to enter a string or char, we have no support for it yet.")
                        elif(Choice2 == 2):
                            try:
                                entry = int(input("Enter an Integer: "))
                                SearchTree.Delete(entry)
                                input("Press [enter] to continue.\n")
                            except ValueError:
                                print("Please enter an integer Value. If you are trying to enter a string or char, we have no support for it yet.")
                        elif(Choice2 == 3):
                            try:
                                entry = int(input("Enter an Integer: "))
                                SearchTree.search(entry)
                                input("Press [enter] to continue.\n")
                            except ValueError:
                                print("Please enter an integer Value. If you are trying to enter a string or char, we have no support for it yet.")
                        elif(Choice2 == 4):
                            SearchTree.TraverseNLR()
                            input("Press [enter] to continue.\n")
                        elif(Choice2 == 5):
                            SearchTree.TraverseLNR()
                            input("Press [enter] to continue.\n")
                        elif(Choice2 == 6):
                            SearchTree.TraverseLRN()
                            input("Press [enter] to continue.\n")
                        elif(Choice2 == 7):
                            SearchTree.Instruction()
                            input("Press [enter] to continue.\n")
                        elif(Choice2 == 8):
                            print("Exiting.")
                            input("Press [enter] to exit.")
                            break
                        else:
                            print("Enter a value that is valid ")
                    except ValueError:
                        print("Please enter an integer Value")
            elif(Choice == 2):
                print("Exiting.")
                input("Press [enter] to exit.")
                break
            else:
                print("Please enter a value from the corresponding choices.")
        except ValueError:
            print("Please enter an integer value.\n")




if __name__ == '__main__':
    main()