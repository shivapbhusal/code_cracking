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

slow=L.head
fast=L.head 

while (fast !=None or fast.next !=None):
    slow=slow.get_next()
    fast=fast.get_next().get_next()
    if (slow==fast):
        break

if fast==None and fast.next==None:
    print('NO')
else:
    print('YES')


slow=L.head

while (slow !=fast):
    slow=slow.get_next()
    fast=fast.get_next()

print(fast.get_data())







