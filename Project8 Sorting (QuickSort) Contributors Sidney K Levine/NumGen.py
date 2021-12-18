

#import
from random import randint
def main():
    #Generate random numbers
    f = open('Onum4.txt','w')

    for i in range(0, 1000):
        f.write('{}\n'.format(i))
    
    f.close()

main()