#Rezvee Rahman
#Node Class
#Note: Can be used for BST, AVL, and Heaps

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None
    
    def __del__(self):
        return None
    
    #def __str__(self):
        #return "the node is {}".format(self)


    #Setters
    def setValue(self, value):
        self.value = value

    def setLeft(self, Left):
        self.left = Left
    
    def setRight(self, Right):
        self.right = Right

    #Getters
    def getValue(self):
        return self.value

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    #left and right pointer tests

    #Checks if any pointer is filled
    def AnyPointersFilled(self):
        if(self.getLeft() is not None or self.getRight() is not None):
            return True
        else:
            return False

    #Checks Left pointer is filled
    def LeftFilled(self):
        if(self.getLeft()):
            return True
        else:
            return False
    
    #Check if Right pointer is filled
    def RightFilled(self):
        if(self.getRight()):
            return True
        else:
            return False
    
    #Check if both pointers are empty
    def BothPointersEmpty(self):
        if(self.getLeft() is None and self.getRight() is None):
            return True
        else:
            return False
    
    #Disconnection (removes the node from the pointers)
    def Disconnect(self):
        self.setRight(None)
        self.setLeft(None)
    

         

    #For Binary Search Tree

    #Traversals (All of these simply are simply the same code but rearragned into different orders)
    def TravNLR(self):
        print(self.getValue(),"\n")
        if(self.LeftFilled()):
            print("going left")
            self.getLeft().TravNLR()
            print("going back")
        if(self.RightFilled()):
            print("going right")
            self.getRight().TravNLR()
            print("going back")

    def TraverseNLR(self):
        element = []
        element.append(self.getValue())
        if(self.LeftFilled()):
            left = self.getLeft().TraverseNLR()
            for i in left:
                element.append(i)
        if(self.RightFilled()):
            right = self.getRight().TraverseNLR()
            for i in right:
                element.append(i)
        return element

    def TraverseLNR(self):
        element = []
        if(self.LeftFilled()):
            left = self.getLeft().TraverseLNR()
            for i in left:
                element.append(i)
        element.append(self.getValue())
        if(self.RightFilled()):
            right = self.getRight().TraverseLNR()
            for i in right:
                element.append(i)
        return element
    
    def TraverseLRN(self):
        element = []
        if(self.LeftFilled()):
            left = self.getLeft().TraverseLRN()
            for i in left:
                element.append(i)
        if(self.RightFilled()):
            right = self.getRight().TraverseLRN()
            for i in right:
                element.append(i)
        element.append(self.getValue())
        return element
    #Insertion for a BST (Will Not insert Duplicates!)
    def BstIns(self, value, root=0):
        if(self.getValue() is value):
            print("Will not insert a duplicate value to a BST")
        else:
            if(value < self.getValue()):
                if(self.getLeft() is None):
                    self.setLeft(Node(value))
                else:
                    self.getLeft().BstIns(value, root)
            else:
                if(self.getRight() is None):
                    self.setRight(Node(value))
                else:
                    self.getRight().BstIns(value, root)

    #Get Maximum
    def getMax(self):
        if(self.getRight() is not None):
            return self.getRight().getMax()
        else:
            return self

    #Get Minimum
    def getMin(self):
        if(self.getLeft() is not None):
            return self.getLeft().getMin()
        else:
            return self
    
    #Search for a value
    def BstSrch(self, value, root=0):
        if(self.getValue() is value):
            print("We found the value.")
            return self
        else:
            
            if(value < root):
                if(self.getLeft() is not None):
                    self.getLeft().BstSrch()
                else:
                    print("We could not find the value you are searching.")    
            else:
                if(self.getRight() is not None):
                    self.getRight().BstSrch()
                else:
                    print("We could not find the value you are searching.")
    
    #Deletion for a Node, used in BST
    def BstDel(self, value, root=0):
        #We are traversing through the tree and updating the links everytime
        if(value < self.getValue()):
            if(self.LeftFilled()):
                self.setLeft(self.getLeft().BstDel(value, root))
                return self #Make sure to return self otherwise we get an error
            else:
                print("We can't find the value to be deleted.")
        elif(value > self.getValue()):
            if(self.RightFilled()):
                self.setRight(self.getRight().BstDel(value, root))
                return self
            else:
                print("We can't find value to be deleted.")
        #This occurs when we found the value of deletion
        else: #So what happens here is we recursively update our tree. Eliminating the Node by return a none value
            #For a specific link in a tree
            if(self.BothPointersEmpty()): #Case 1 Leaf Node
                return None #Return None
            elif(self.LeftFilled() and not self.RightFilled()): #Case 2A Left Side is occupied
                return self.getLeft()#Just return the left side
            elif(self.RightFilled() and not self.LeftFilled()):#Case 2B Right side is occupied
                return self.getRight()#Just return the right side
            else:#Case 3 both sides are occupied
                if(value < root):#If the value is less than the root we know it is the left of the BST
                    UpdatedNode = self.getMax()
                    self.BstDel(UpdatedNode.getValue(), self.getValue())
                    BranchLeft = self.getLeft()
                    BranchRight = self.getRight()

                    #Update the 2 children node with the max

                else: #If the value is greater than the root then we know it is the right of the BST
                    #The same logic applies here except our value is greater than root
                    #We get the minimum
                    UpdatedNode = self.getMin()
                    self.BstDel(UpdatedNode.getValue(), self.getValue())
                    BranchLeft = self.getLeft()
                    BranchRight = self.getRight()
                
                UpdatedNode.setLeft(BranchLeft)
                UpdatedNode.setRight(BranchRight)
                return UpdatedNode
                
                #SPECIAL Note of the Delete: We are recursively updating our tree everytime we call this function.
                #Although there still some things I have to mention
                #Python does not allow us to force an object to be deleted
                #When the program is finished executing Garbage collection is done automatically
                #There was a shortcomming in the original program where I tried to force python delete an object  
                    

