# A program to remove duplicates from the singly linked list 
import sys 
sys.path.insert(0,'/home/civaist/Documents/Others/code_cracking/Linked_Lists')

from linked_list import LinkedList
from linked_list import Node 
	
def deleteMiddle(L,myNode):
    current=L.head 
    prev=None 
    while(current):
    	if current.get_data()==myNode.get_data():
    		prev.next_node=current.next_node
    		return 
    	prev=current 
    	current=current.get_next()

L=LinkedList()

for i in range(1,10):
    L.insert(i)

myNode=Node(5)
deleteMiddle(L,myNode)

L.read()







