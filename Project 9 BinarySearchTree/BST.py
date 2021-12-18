#Binary Search Tree implmentation

#Imports
from Node import Node

class BST:
    
    def __init__(self) -> None:
        self.root = None

    def __del__(self):
        return None
    
    def __str__(self) -> str:
        return "The Binary Search Tree starts with the root {}".format(self.root)
    
    #Setters
    def setRoot(self, root):
        self.root = Node(root)
    
    #Getters
    def getRoot(self):
        return self.root

    
    #Methods
    def insert(self, value):
        if(self.getRoot() is None):
            self.setRoot(value)
        else: 
            self.getRoot().BstIns(value, self.getRoot().getValue())

    def search(self, value):
        if(self.getRoot().getValue() is value):
            return self.getRoot()
        else:
            self.getRoot().BstSrch(value, self.getRoot().getValue())

    def Delete(self, value):
        #Usually deleting the root will require us to get the right most minimum
        if(self.getRoot().getValue() is value): 
            if(self.getRoot().RightFilled()):
                print("Case 1")
                #Find the minimum
                newNode = self.getRoot().getRight().getMin()
                #Update the right side of the tree
                RightC = self.getRoot().getRight().BstDel(newNode.getValue(), self.getRoot().getValue())
                #Get the left side aswell(it can be none)
                LeftC = self.getRoot().getLeft()

            elif(self.getRoot().LeftFilled()): #If there is no Right then use the left
                print("Case 2")
                newNode = self.getRoot().getLeft().getMax()
                LeftC = self.getRoot().getLeft().BstDel(newNode.getValue(), self.getRoot().getValue())

                RightC = self.getRoot().getRight()
            else:
                print("Case 3")
                newNode = None
                LeftC = self.getRoot().getLeft()
                RightC = self.getRoot().getRight()
            
            self.root = newNode
            if(self.getRoot() is not None):
                print("pass")
                self.getRoot().setRight(RightC)
                self.getRoot().setLeft(LeftC)
        else:
            self.getRoot().BstDel(value, self.getRoot().getValue())
    


    def TraverseNLR(self):
        if(self.getRoot() is None):
            print("We can't Traverse an empty tree.")
        else:
            print(self.getRoot().TraverseNLR())
    
    def TraverseLNR(self):
        if(self.getRoot() is None):
            print("We can't Traverse an Empty tree.")
        else:
            print(self.getRoot().TraverseLNR())

    def TraverseLRN(self):
        if(self.getRoot() is None):
            print("We can't Traverse an empty tree,")
        else:
            print(self.getRoot().TraverseLRN())
        
    def Instruction(self):
        if(self.getRoot() is None):
            print("We can't Traverse an Empty tree")
        else:
            self.getRoot().TravNLR()