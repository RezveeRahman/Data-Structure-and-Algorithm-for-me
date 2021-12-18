#Rezvee Rahmna
#CSC212-03
#Stacks Class

class Stacks:
    #Initialize special Stack, Queue, Double Queue
    def __init__(self):
        self._stack = []
        pass

    def __str__(self):
        return "The following is contained in the stack \n{}".format(self._stack)
        
    #Methods that can be passed to other stack classes
    #______________________________________________________________________________
    #This will return the length of a stack. Potentially used for Queue and D_Queue
    def __len__(self):
        return len(self._stack)

    #This will return a boolean value. If empty then True, if not empty then False
    def stack_empty(self):
        return len(self._stack) == 0
    #--------------------------------------------------------------------------------

    #Methods that will not be passed! Exclusive for this class
    #_______________________________________________________________________________
    #This method will push an element in the stack
    def push(self,_newdata):
        self._stack.append(_newdata)
        return self._stack

    #Pop method will remove element in the stack. Note that the last element is removed or what is on top of the stack
    def pop(self):
        if(len(self._stack) == 0):
            print("Stack is Empty")
            return None
        else:
            self._stack.pop()
            return self._stack
    
    #Will return the top of the stack. Using -1 will always return the last element.
    def Top(self):
        return self._stack[-1]
    
    #Will look at a certain index in the stack and return the value
    def Peek(self,index):
        if(self.stack_empty() == False):
            try:
                return self._stack[index]
            except IndexError:
                print("The index entered is invalid. Enter integer value or check the length of the stack.")
        else:
            print("Stack is empty.")
    

    
    
    

