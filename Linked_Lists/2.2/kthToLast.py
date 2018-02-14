# A program to remove duplicates from the singly linked list 
import sys 
sys.path.insert(0,'/home/civaist/Documents/Others/code_cracking/Linked_Lists')

from linked_list import LinkedList
	
def readKthToEnd(L,k):
    current=L.head 
    count=1
    while(current):
        if count>=k:
            print(current.get_data())
        count=count+1 
        current=current.get_next()

L=LinkedList()

for i in range(1,10):
    L.insert(i)

readKthToEnd(L,1)
print("/n")

readKthToEnd(L,5)








