# A program to partition a Linked List in two parts 

import sys 
sys.path.insert(0,'/home/civaist/Documents/Others/code_cracking/Linked_Lists')

from linked_list import LinkedList
from linked_list import Node

class Stack:   # Creation of a stack class 

    def __init__(self): # constructor that creates myStack, an empty list. 
        self.mystack=[]

    def is_empty(self):     # If the stack is empty, return False Else Return True 
        return self.size()==0
                                         
    def push(self, x):      # Append item at the end of the list 
        self.mystack.append(x) 

    def pop(self):
        return self.mystack.pop()  # Pop the last element of the List

    def size(self):              # Return the length of the List 
        return len(self.mystack)


def getString(L):
    myStr=''
    current=L.head
    while (current):
        myStr=myStr+str(current.get_data())
        current=current.get_next()
    return myStr

L1=LinkedList()

for i in ['a','b','c']:
    L1.insert(i)

myStr=getString(L1)
myStack=Stack()

for chars in myStr:
    myStack.push(chars)

str2=''
while(not (myStack.is_empty())):
    str2=str2+str(myStack.pop())

if myStr==str2:
    print('Yes')
else:
    print('No')
    









