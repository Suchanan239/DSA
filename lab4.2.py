class ArrayStack:
    def __init__(self):
        #create stack
        self.data = []
    
    def size(self):
        return (len(self.data))
    
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
 
def copyStack(stack1, stack2):
    stack3 = ArrayStack()
    while stack2.data != []:
        stack2.pop()
    while stack1.data != []:
        x = stack1.stackTop()
        stack1.pop()
        stack3.push(x)
    while stack3.data != []:
        x = stack3.stackTop()
        stack3.pop()
        stack1.push(x)
        stack2.push(x)
    return (stack1.data, stack2.data)

 

s1 = ArrayStack()
s2 = ArrayStack()
s1.push(10), s1.push(20), s1.push(30)
s2.push(15)
copyStack(s1, s2)
s1.printStack()
s2.printStack()