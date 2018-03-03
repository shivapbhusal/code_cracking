# A program to partition a Linked List in two parts 

import sys 
sys.path.insert(0,'/home/civaist/Documents/Others/code_cracking/Linked_Lists')

from linked_list import LinkedList
from linked_list import Node 

L=LinkedList()

for i in range(1,5):
    L.insert(i)

current=L.head

while (current.get_data()!=1):
    current=current.get_next()
    if current.get_data()==1:
        current.set_next(L.head)

L.read()









