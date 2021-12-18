#Rezvee Rahman
#THIS FILE IS FOR "StateGuessGame.py" it is for pickling data
#IMPORTS
from os import close
import pickle
from typing import Dict

#GLOBABL VARIABLES FOR TESTING


#read function, will check if file is found and ready for pickling
def openFileR():
    InFile = input("Enter the file name and extension [e.g. Test.txt]: ")
    try:
        OpenedFile = open(InFile,'r')
        return OpenedFile
    except Exception:
        print("Could not find file!")
        return "NULL"

def openFileRB():
    InFile = input("Enter the file name and extension (note this is for binary files only!) [e.g. Test.txt]: ")
    try:
        OpenedFile = open(InFile, 'rb')
        return(OpenedFile)
    except Exception:
        print("This file is not in Binary, or doesn't Exist!")
        return"NULL"


#will loop through the file and return a dictionary
def fileConversionDict(OFile_P):
    if(OFile_P != "NULL"):

        #We initialize a dictionary object
        file_dictionary = dict()

        #Loop through all lines
        for item in OFile_P:
            Listeditem = OFile_P.readline()

            #===================Strip and Split
            Stripped = Listeditem.strip('\n')
            Splitted = Stripped.split(',')
            #===================================

            print(Splitted)
            Capital = Splitted[0]
            State = Splitted[1]  
            #Adding new data entry
            file_dictionary[State] = Capital
        #print (file_dictionary)
        OFile_P.close()
        return file_dictionary
    else:
        print("Please enter a valid File.")
        return 0


#We will pickle our data and return it as a binary file
def filepickling(Output_info):
    Output_file = open('DictBin.dat','wb')
    pickle.dump(Output_info, Output_file)
    Output_file.close()
    print("Pickling successful, check file!")
    return 0

def unpickle_data(File_name):
    if(File_name != "NULL"):
        unpickle_file = pickle.load(File_name)
        #print(unpickle_file)
        return unpickle_file

#note: for future debugging please remove the comment pound symbol for the print functions
#The functions to pickle a file
#Open readable text file ---> Convert each line to a set ---> Pickle the file/convert binary
#filepickling(fileConversionDict(openFileR()))