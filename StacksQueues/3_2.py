'''
Question no. 3.2:
Implementing a stack to get the minimum element in a stack.
Push, Pull and Min operations should operate in O(1) time.
'''

import math

class Stack():
    def __init__(self):
        self.stack = []
        self.min_element=[]

    def push(self, x):
        self.stack.append(x)
        if len(self.min_element) == 0:
            self.min_element.append(x)
        else:
            if x < self.min_element[len(self.min_element)-1]:
                self.min_element.append(x)
            else:
                self.min_element.append(self.min_element[len(self.min_element)-1])

    def pop(self):
        if len(self.stack):
            self.min_element.pop()
            return self.stack[0]

    def getSize(self):
        return len(self.stack)

    def getMinElement(self):
        return self.min_element[len(self.min_element)-1]
        
s = Stack()

for i in range(5,10):
    s.push(i)

for i  in range(0,5):
    s.push(i)

for i in range(7):
    print(s.getMinElement())
    s.pop()

