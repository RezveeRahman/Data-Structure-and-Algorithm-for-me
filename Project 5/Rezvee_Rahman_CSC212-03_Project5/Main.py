#Rezvee Rahman
#CSC212-03
#Project 5 Stacks

#Imports
import Stacks


def main():
    print("Postfix math expression solver.\n")
    while True:
        try:
            print("Menu options\n1 - Solve a math expression\n2 - Exit\n")
            choice = int(input("Please enter your choice: "))

            if(choice == 1):
                mathStack = Stacks.Stacks()
                historyStack = Stacks.Stacks()
                operatorList = ["*","/","+","-"]
                counter = 0
                print("Please enter the 2 starting numbers in your postfix expression.\n")
                while counter < 2:
                    try:
                        ValueEntry = float(input("number: "))
                        mathStack.push(ValueEntry)
                        historyStack.push(ValueEntry)
                        counter += 1
                    except ValueError:
                        print("You must enter a integer or float value!\n")
                print("Current Stack is {}".format(mathStack))
                
                

                while True:
                    print("here are some valid operations you can put into your stack to solve (+, -, *, /,).")
                    choice_2 = input("What operations or Operands would you like to add? to exit the stack hit enter without any text or spaces: ")
                    if(choice_2 == ""):
                        print("Breaking from the operation.\n")
                        break
                    elif((choice_2 in operatorList) and (mathStack.__len__() >= 2)):
                        #remove from the top of the stack
                        a = mathStack.Top()
                        mathStack.pop()
                        b = mathStack.Top()
                        mathStack.pop()
                        #Mult
                        if(choice_2 == operatorList[0]):
                            mathStack.push(a.__mul__(b)) 
                            historyStack.push("*")
                        #Div: Potential error here. If we divide 5/3 we get a float not an int                      
                        elif(choice_2 == operatorList[1]):
                            mathStack.push(a.__truediv__(b))
                            historyStack.push("/")
                        #Add
                        elif(choice_2 == operatorList[2]):
                            mathStack.push(a.__add__(b))
                            historyStack.push("+")
                        #Subtract
                        else:
                            mathStack.push(a.__add__(-b))
                            historyStack.push("-")
                    else:
                        try:
                            mathStack.push(float(choice_2))
                            historyStack.push(float(choice_2))
                        except ValueError:
                            print("Either the stack doesn't have enough values in or this entry is not correct try again.\n")
                            input("Press Enter key to continue: ")
                    
                    print(mathStack)

                print("\n")
                print("The Final Stack. {}\nThe Historical stack. {}".format(mathStack, historyStack))

                
            elif(choice == 2):
                print("Exiting program.")
                break
            else:
                print("Entry is invalid try again.\n")
    
        except ValueError:
            print("Entry is not an integer value.\n")
       

if __name__ == "__main__":
    main()
    pass
