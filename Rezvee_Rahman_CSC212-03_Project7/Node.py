#Rezvee Rahman
#CSC212-03
#Nodes

#Imports

class Nodes:
    #=================================================
    #Our node class will have the following elements
        #Data: holds a value
        #Pointer/next: This will point to another node
    #=================================================

    def __init__(self, data):
        self.data = data
        self.pointer = None
    
    #Getters
     #=================================================
    #Get our Data value in a node                     
    def getNode(self):                               
        return self.data

    #Get our next node
    def getNext(self):
        return self.pointer
     #=================================================
    
    #Setters
    #=================================================
    #Set our Node data
    def _setNode(self, dataEntry):
        self.data = dataEntry
    
    #Set our Next/pointer for a data
    def _setNext(self, nodeEntry):
        if nodeEntry == Nodes:
            print("Can't connect to data because it is not a node class")
        else:
            self.data = Nodes(nodeEntry)
     #=================================================