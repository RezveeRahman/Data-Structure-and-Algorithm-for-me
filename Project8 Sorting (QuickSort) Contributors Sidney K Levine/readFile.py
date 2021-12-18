#Slightly modified
#Introduced striponly
#changed the line returner to accomomdate integers
def readfile_():
    file = input("Please enter the file you want to read [Case sensitive with extension]: ")
    try:
        opened_file = open(file,'r')
        return opened_file
    except FileNotFoundError:
        print("File could not be found")
        pass

def lineReturner(filename):
    L_ = []
    for i in filename:
        L_.append(int(striponly(i)))    
    return L_
    


def splitandstrip(line):
    return line.strip('\n').split(" ")

def striponly(line):
    return line.strip("\n")
