#Rezvee Rahman
#CSC212-03
#Unordered Linked List

#imports potentially for inheritance
#import Node 
from Node import Node

class UnLi(Node):
    def __init__(self):
        #The pointer of a unordered list starts as none 
        self.head = None

    #Modify, this is an important step. We have to start with our
    #
    def add(self, item):
        temp = Node(item)
        temp._set_next(self.head)
        self.head = temp #Everytime we add a new item it becomes the head
        
    
    def remove(self, item):
        current = self.head
        previous = None
        found = False

        while not found:

            if(current._get_node() == item):
                found = True
            else:
                previous = current
                current = current._get_next()
        if(previous == None):
            self.head = current._get_next()
        else:
            previous._set_next(current._get_next())
        


    #Information
    #====================================
    #This is an empty unordered link list
    def _isEmpty(self):
        #Returns Boolean Value
        return self.head == None
    
    #Size of an Unordered Linked list
    def _size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current._get_next() #The _getNext
        return count
    
    def search(self, item):
        #Start from the head
        current = self.head
        found = False #Set our found value to be be none

        #Iterate through the loop until we find our value
        #Note if it isn't found we should return none
        while current != None and (not found):
            if (current._get_node() == item):
                found = True
            elif(current._get_node() == None):
                print("No value found")
            else:
                current = current._get_next()
        return found

            

    