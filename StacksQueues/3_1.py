'''
Page 98: Question no 3.1.
Implementing three stacks using a single array.
'''

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)
        print(x, 'pushed to stack')

    def pop(self):
        if len(self.stack):
            return self.stack.pop(0)

    def getSize(self):
        return len(self.stack)

s = Stack()



