from Node import Node
from BST import BST

Ts = BST()

#app = [17, 5, 11, 35, 2, 38, 29, 16, 9, 8, 40]
#app = [25, 15, 10]
app = [17, 5, 11, 2, 9, 8, 16]

for i in range(0, len(app)):
    Ts.insert(app[i])

Ts.Delete(17)
Ts.Delete(5)
Ts.TraverseLRN()
Ts.Delete(11)


#print(Ts.getRoot().getRight().R#ightFilled())
#print(Ts.getRoot().LeftFilled())
#print(Ts.getRoot().getLeft())

#Ts.Delete(35)

