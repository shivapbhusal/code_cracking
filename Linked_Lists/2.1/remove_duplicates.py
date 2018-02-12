# A program to remove duplicates from the singly linked list 
import sys 
sys.path.insert(0,'/home/civaist/Documents/Others/code_cracking/Linked_Lists')

from linked_list import LinkedList

L=LinkedList()

for i in range(10):
    L.insert(i)

for i in range(5):
	L.insert(i)

finalList=LinkedList()

current1=L.head
current2=L.head 
while (current1):
	count=1
	while(current2):
		if current1==current2:
			count=count+1
		current2=current2.get_next()
	if count>1:
		finalList.insert(current1.get_data())

	current1=current1.get_next()

finalList.read()





