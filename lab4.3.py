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
        #check the top of stack
        if self.data == []:
            return None
        else:
            data = self.data[-1]
            return data
        
    def printStack(self):
        #print stack
        print(self.data)
 
def copyStack(stack1, stack2):
    #copy data from stack1 to stack2
    stack3 = ArrayStack()
    while stack2.data != []:
        stack2.pop()
    while stack1.data != []:
        x = stack1.data[-1]
        stack1.pop()
        stack3.push(x)
    while stack3.data != []:
        x = stack3.data[-1]
        stack3.pop()
        stack1.push(x)
        stack2.push(x)
    return (stack1.data, stack2.data)

def infixToPostfix(expression):
    stack = ArrayStack()
    postfix = ""
    for i in expression:
        if i.isalpha() == True:
            postfix += i
        elif i in '+-*/':
            if stack.is_empty():
                stack.push(i)
            else:
                if i in '+-':
                    while not stack.is_empty():
                        postfix += stack.pop()
                    stack.push(i)
                elif i in '*/':
                    if stack.stackTop() in '+-':
                        stack.push(i)
                    else:
                        while not stack.is_empty():
                            postfix += stack.pop()
                        stack.push(i)
    while not stack.is_empty():
        postfix += stack.pop()
        
    return postfix
            
exp = 'A/B*C/D'
postfix = infixToPostfix(exp)
print('Postfix of', exp, 'is', postfix)
