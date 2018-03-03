# A program to partition a Linked List in two parts 

import sys 
sys.path.insert(0,'/home/civaist/Documents/Others/code_cracking/Linked_Lists')

from linked_list import LinkedList
from linked_list import Node 

def makeList(N,size):
    L=LinkedList()
    position=10
    rem=0
    while(N!=0):
        rem=int(N)%int(position)
        N=int(N/position)
        L.insert(rem)
    return L 

def getNumber(L,size):
    current=L.head
    number=0
    position=1
    for i in range(size-1):
        position=position*10

    while (current):
        number=number+int(current.data)*position
        current=current.get_next()
        position=position/10
    return int(number)

def getSize(L):
    current=L.head 
    size=0
    while(current):
        size=size+1
        current=current.get_next()
    return size

L1=LinkedList()
L2=LinkedList()

for i in range(1,5):
    L1.insert(i)

for i in range(1,5):
    L2.insert(i)

L1.read()
L2.read()

result=getNumber(L1,getSize(L1))+getNumber(L2,getSize(L2))

size=len(str(result))

finalList=makeList(result,size)
finalList.read()










