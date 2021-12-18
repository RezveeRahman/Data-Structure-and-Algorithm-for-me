#Rezvee Rahman
#CSC212-03
#Linked List

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
        self.pointer = nodeEntry
     #=================================================

#=================================================
class UnLi:

    #Initialization of a unordered list
    def __init__(self):
        #When we start a unordered list we need to make a head for the list
        #This will serve has the basis
        self.head = None

    #Modification Methods for Our unordered List
    #Append is special dunder because it will have differrent algorithmic implementation
    def _append(self, dataItem):
        temporary = Nodes(dataItem)
        temporary._setNext(self.head)
        self.head = temporary

    def remove(self, dataItem):
        current = self.head
        previous = None
        found = False
        while not found and current != None:
            if(current.getNode() == dataItem):
                found = True
            else:
                previous = current
                current = current.getNext()
        
        #Current is not none then we found a node to be removed
        if(current != None):
            if(previous == None):
                self.head = current.getNext()
            else:
                previous._setNext(current.getNext())
        else:
            print("Could not find Node.")

    #Information Methods For Our unordered List
    #Returns Bool if list is empty or not
    def isEmpty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0

        while current != None:
            count += 1
            current = current.getNext()
        return count

    def _search(self, Value):
        current = self.head #Start with the head of the linkedlist
        found = False
        while current != None and not found:
            if(current.getNode != None):
                if(current.getNode() == Value):
                    found = True
                else:
                    current = current.getNext()
            else:
                print("The value could not be found in the linked list!\nCheck if there are any values in link list chain.")
        return found
    
    #Will return a chain of values
    def _getLink(self):
        #We will go over the entire linked list O(n) time 

        #Start with the head
        current = self.head

        #Counter value
        Count = 0

        if(self.head == None):
            print("We either reached the end of the linked list or Have no data.")
        elif(self.head != None):
            for i in range(0, self.size()):
                Count += 1
                print("{}. {}".format(Count, current.getNode()))
                current = current.getNext()
        else:
            print("Unexpected error has occured")


class OrLi(UnLi): #This is a sub class of unordered linked list

    #Initialization of Ordered List
    def __init__(self):
        super().__init__()


    def _append(self, Val):
        #New value to be inserted
        #Current position of the list
        current = self.head

        #Previous Node, When starting it is None
        previous = None

        #Stop will act as conditional variable
        Stop = False

        #Determine Positioning of the Ordered linked List
        while current != None and not Stop:
            if(current.getNode() > Val):
                Stop = True
            else:
                previous = current
                current = current.getNext()
        
        NewInsert = Nodes(Val)
        #Here is the check
        if previous == None: #If our linked list is empty then insert here
            NewInsert._setNext(self.head) #set the none
            self.head = NewInsert #set the head as the new entry  

        #If the previous statement is not the case then do this instead
        else:
            NewInsert._setNext(current) #Set the current value
            previous._setNext(NewInsert)

    def _search(self, value):
        current = self.head
        found = False
        stop = False

        #The concept is similar to the unordered list search. However it is modified
        while current != None and not found and not stop:
            #If we found the node we are looking for then stop
            if(current.getNode() == value):
                found = True
            #If not then continue
            else:
                #if the value of the node exceeds the current value then stop
                if current.getNode() > value:
                    stop = True
                    print("Our ordered linked list shows that we have not found the node.\nTherefore it may not exist in the linked list.")
                else:
                    #if the previous if statement didn't work then get the next node
                    current = current.getNext()
        #Based on the algorithm above.
        #found is false by default but if the algorithm found the required value it returns true
        #Boolean return
        return found