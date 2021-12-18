#Rezvee Rahman
#CSC212-03
#Openfile

#===================================
def _openfile_read(filename):
    try:
        openedfile = open(filename,'r')
        return openedfile
    except FileNotFoundError:
        print("File is not found!")
        return None
#===================================

#===================================
def _readfilevalues(filename):
    #List that gives the final list
    retlist = []

    if(filename == None):
        print("Can't read file")
    else:
        for i in filename:
            #Split each values in the file. This will be important later
            split = str(i).strip('\n').split(" ")
            retlist.append(split)
        print(retlist)
        return retlist
#===================================        

            