class ArrayStack:
    def __init__(self):
        #create stack
        self.data = []
    
    def size(self):
        print(len(self.data))
    
    def is_empty(self):
        if self.data == []:
            return True
        else:
            return False
        
    def push(self, data):
        #push data into myStack
        self.data.append(data)
    
    def pop(self):
        #pop the lastest data out of stack
        if self.data == []:
            print("Underflow: Cannot pop data from an empty list")
        else:
            data = self.data[-1]
            self.data.pop()
            return data
    
    def stackTop(self):
        if self.data == []:
            return None
        else:
            data = self.data[-1]
            return data
        
    def printStack(self):
        print(self.data)

myStack = ArrayStack()
myStack.push(10), myStack.push(20), myStack.push(30)
myStack.printStack()
x = myStack.pop()
print(x)
myStack.pop()
myStack.printStack()
myStack.pop()
print(myStack.is_empty())
myStack.pop()
myStack.size()
