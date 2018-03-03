# A program to partition a Linked List in two parts 

import sys 
sys.path.insert(0,'/home/civaist/Documents/Others/code_cracking/Linked_Lists')

from linked_list import LinkedList
from linked_list import Node 


def getNumber(L):
    current=L.head
    number=0
    position=1
    while (current):
        number=number+int(current.data)*position
        position=position*10
        current=current.get_next()
    return number



L1=LinkedList()
L2=LinkedList()

for i in range(1,5):
    L1.insert(i)

for i in range(1,5):
    L2.insert(i)

L1.read()
L2.read()

print(getNumber(L1)+getNumber(L2))

#myNode=Node(5)
#deleteMiddle(L,myNode)







