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

    def is_parentheses_matching(self, expression):
        for i in expression:
            if i == '(':
                self.data.append('(')
            elif i == ')':
                self.data.pop()
        
        if self.data == []:
            print('Parentheses in '+expression+' are matched')
            return True
        else:
            print('Parentheses in '+expression+' are unmatched')
            return False
        
myStack = ArrayStack()
strr = "((A-B)*C)"
result = myStack.is_parentheses_matching(strr)
print(result)
