# A program to remove duplicates from the singly linked list 
import sys 
sys.path.insert(0,'/home/civaist/Documents/Others/code_cracking/Linked_Lists')

from linked_list import LinkedList
from linked_list import Node 
	
def deleteMiddle(L,myNode):
    myNode.data=myNode.get_next().data
    myNode.next_node=myNode.get_next().get_next()

L=LinkedList()

for i in range(1,10):
    L.insert(i)

current=L.head 
myNode=current.get_next()
myNode=myNode.get_next() 

deleteMiddle(L,myNode)

L.read()







