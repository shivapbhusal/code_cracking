# A program to remove duplicates from the singly linked list 
import sys 
sys.path.insert(0,'/home/civaist/Documents/Others/code_cracking/Linked_Lists')

from linked_list import LinkedList

def insertUnique(data,uniqueList):
	current=uniqueList.head
	while (current):
		if current.get_data()==data:
			return None
		current=current.get_next() 
	uniqueList.insert(data)
	

L=LinkedList()

for i in range(10):
    L.insert(i)

for i in range(5):
	L.insert(i)

uniqueList=LinkedList()

current=L.head 
while (current):
	insertUnique(current.get_data(),uniqueList)
	current=current.get_next()

uniqueList.read()








