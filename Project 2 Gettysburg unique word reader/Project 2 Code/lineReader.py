#Rezvee Rahman
#CSC212-03
#Project 2
#Import file


#Select the file to read
def readSelectFile():
    return input("Type in the file you want to read [Case Sensitive]: ")

#read line of file and return it as a string
def line_read(file): 
    #read method
    Selectedfile = open(file ,'r')
   
   #replace commas with whitespace
    List_Txt = Selectedfile.read().replace(',','').replace('.','').split()
    
    #Returns a list
    return List_Txt


def count_words_unique(ListofWords):

    #Using set will get rid of duplicate words
    UniqueSet = set()

    #Go through each item in a list
    for i in ListofWords:
        #Add them in the set
        UniqueSet.add(i)
        #Discard character such as 
        UniqueSet.discard("--")

        #print(i)
    print(UniqueSet)
    print("\nThere are {} unique words found in this Text!".format(len(UniqueSet)))

    return 0