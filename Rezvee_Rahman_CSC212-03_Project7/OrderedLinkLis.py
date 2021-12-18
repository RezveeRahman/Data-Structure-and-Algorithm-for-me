#Rezvee Rahman
#CSC212-03
#Ordered Link List

#import node is required
from typing import ItemsView
import Node

class OrderedLinkLis:

    #Instance of the ordered list
    def __init__(self):
        self.head = None
    
#Modification to ordered linkled list
    #Unlike the unordered linked list this one will be slightly different
    def _add(self, item):
        current = self.head
        previous = None
        halt = False
        while current != None and not halt:
            if(current._get_node() > item):
                halt = True
            else:
                previous = current
                current = current._get_node()

        temp = Node(item)

        if(previous == None):
            temp._set_nd()
            self.head = temp
        else:
            temp._set_next(self.head)
            previous._set_next(temp)

    #Remove
    def _remove(self, item):
        current = self.head
        previous = None
        found = False

        while not found:
            if(current._get_nd() == item):
                found = True
            else:
                previous = current
                current = current._get_next()

        if previous == None:
            self.head = current._get_next()
        else:
            previous._set_next(current._get_next())
             

#Information From an ordered linked list

    #Searching in the ordered linked list
    def search(self, item):
        current = self.head
        found = False
        halt = False

        while current != None and not found and not halt:
            if(current._get_node() == item):
                found = True
            else:
                if current._get_node() > item:
                    stop = True
                else:
                    current = current._get_next()

        return found

    #Is the linked list empty?
    def _isEmpty(self):
        return self.head == None
    
    #What is the size of the linked list?
    def _size(self):
        current = self.head
        count = 0

        while current != None:
            count += 1
            current = current._get_next()
    
        return count


    