# A program to remove duplicates from the singly linked list 
import sys 
sys.path.insert(0,'/home/civaist/Documents/Others/code_cracking/Linked_Lists')

from linked_list import LinkedList

L=LinkedList()

for i in range(10):
    L.insert(i)

for i in range(5):
	L.insert(i)

current=L.head  
temp_buffer=[] 

while (current):
	if current.get_data() in temp_buffer:
		L.delete(current.get_data())
	else:
		temp_buffer.append(current.get_data())
		
	current=current.get_next() 

L.read()








