#Rezvee Rahman
#CSC212-03
#Project 6 Queues

#Imports
import Queues

def main():
    print("Queue Prefix math solver.\n")
    while True:
        print("Please enter a value corresponding with the menu option. \n")

        print("\t 1 - Prefix mathsolver")
        print("\t 2 - Exit\n")       
        try:

            #USER INPUT
            option = int(input("Enter your choice: "))

            #IF USER INPUT IS 1 THEN INITIATE PROGRAM
            if(option == 1):

                #Operators List will be used as a comparison for entries in the Queue
                Operators = ["*","/","+","-"]

                #CREATE THE MATH QUEUE AND A TEMPORARY QUEUE
                MathPrefixQ = Queues.Queue()
                TemporaryQ = Queues.Queue()
                

                #VALUE FOR THE USER TO MAKE ENTRIES
                Value = None

                #This will be used for a loop
                OperatorCount = 0
                
                #User enter prefix numbers
                while True:
                    try:
                        Value = input("Enter your Prefix [Press enter to finish]: ")
                        if(Value == ""):
                            print("Exiting.")
                            break
                        elif(Value in Operators):
                            MathPrefixQ._enqueue(Value)
                            OperatorCount += 1
                        else:
                            MathPrefixQ._enqueue(float(Value))
                        print("{}".format(MathPrefixQ))   
                    except ValueError:
                        print("Enter a operand or Operator.\n")
                
                #We will iterate the program multiple times depending on the operators that are present.
                for i in range(0, OperatorCount + 1):
                    #print("Temp {}".format(TemporaryQ)) use this for error checking
                    #print("Main {}".format(MathPrefixQ)) use this for error checking

                    #In each iteration we will go over the Main queue and any operation done will be then transfered to the main queue. 
                    #Also any operations not done will unqueue the current first value 
                    for i2 in range(0, MathPrefixQ._size()-2):
                        #Checks if Main queue is greater than 3 otherwise we will run into an index error
                        if(MathPrefixQ._size() >= 3):
                            #Peek the first element as operator, 2nd element and 3rd element as operators 
                            if( (MathPrefixQ._peek(0) in Operators) and (MathPrefixQ._peek(1) not in Operators) and (MathPrefixQ._peek(2) not in Operators)):
                                #Now we set those values as variables
                                Oper, Num1, Num2 = MathPrefixQ._peek(0), MathPrefixQ._peek(1), MathPrefixQ._peek(2)
                                #Once the criteria has been met by the if-statement above we then do our operations
                                for i in range(0, 3):
                                    MathPrefixQ._unqueue()
                                #Do the operation
                                if(Oper == Operators[0]):
                                    TemporaryQ._enqueue(Num1.__mul__(Num2))
                                elif(Oper == Operators[1]):
                                    TemporaryQ._enqueue(Num1.__div__(Num2))
                                elif(Oper == Operators[2]):
                                    TemporaryQ._enqueue(Num1.__add__(Num2))
                                else:
                                    TemporaryQ._enqueue(Num1.__sub__(Num2))
                            else:
                                TemporaryQ._enqueue(MathPrefixQ._peek(0))
                                MathPrefixQ._unqueue()

                            for i in range(0 , TemporaryQ._size()): #This will return everything back in the main queue  
                                MathPrefixQ._enqueue(TemporaryQ._peek(0))  
                                TemporaryQ._unqueue()
                print(MathPrefixQ)

                                 
            elif(option == 2):
                print("Exiting.")
                break
            else:
                print("Please enter a proper value that aligns with the menu.")
        except ValueError:
            print("Please enter a value that is an integer.")



#Execute the main
if __name__ == '__main__':
    main()