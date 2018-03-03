'''
Python Implementation of Stack. 
Author, Shiva Bhusal, BGSU
'''

class Stack:
    def init(self):
        self.stack=[]

    def isEmpty(self):
        return self.size()==0

    def push(self,x):
        self.stack.append(x)

    def pop(self):
        return self.stack.pop()

    def size(self):
        return len(self.stack)





