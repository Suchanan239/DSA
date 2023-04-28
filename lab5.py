class BSTNode:
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    
    def __init__(self):
        self.root = None
    
    def is_empty(self):
        if self.root == None:
            return True
        else:
            return False
    
    def traverse(self):
        if self.is_empty() == True:
            print('this is an empty tree!!')
        
        else:
            print('Preorder: ')
            self.preorder(self.root)
            print('\nInorder: ')
            self.inorder(self.root)
            print('\nPostorder: ')
            self.postorder(self.root)
            print('\n', end='')

    def insert(self, data):
        pNew = BSTNode(data)
        if self.is_empty() == True:
            self.root = pNew
        else:
            start = self.root
            prev = self.root
            while start != None:
                if data < start.data:
                    prev = start
                    start = start.left
                else:
                    prev = start
                    start = start.right
            if data < prev.data:
                prev.left = pNew
            else:
                prev.right = pNew
        return
        
    def findMin(self):
        start = self.root
        prev = self.root
        if self.is_empty() == True:
            print('this is an empty tree!!')
        elif start.left == None:
            print('Min: ', start.data)
        else:
            while start != None:
                prev = start
                start = start.left
            print('Min: ', prev.data)
        return
    
    def findMax(self):
        start = self.root
        prev = self.root
        if self.is_empty() == True:
            print('this is an empty tree!!')
        elif start.right == None:
            print('Max: ', start.data)
        else:
            while start != None:
                prev = start
                start = start.right
            print('Max: ', prev.data)
        return
    
    def delete(self, data):
        if self.root.data == data and self.root.left == None and self.root.right == None:
            self.root = None
        elif self.is_empty() == True:
            print('cannot delete, this is an empty tree!!')
            return None
        else:
            start = self.root
            prev = self.root
            while start.data != data:
                if data < start.data:
                    prev = start
                    start = start.left
                else:
                    prev = start
                    start = start.right
            if start.left == None and start.right == None:
                if prev.left == start:
                    prev.left = None
                else:
                    prev.right = None
                del start
            elif start.left != None and start.right == None:
                if prev.left == start:
                    prev.left = start.left
                else:
                    prev.right = start.left
                del start
            elif start.left == None and start.right != None:
                if prev.left == start:
                    prev.left = start.right
                else:
                    prev.right = start.right
                del start
            elif start.left != None and start.right != None:
                start = start.left
                while start.right != None:
                    pointer = start
                    start = start.right
                prev.data = start.data
                pointer.right = None
                del start
                    
        return
                


    def preorder(self, root):
        if root != None:
            print('->', root.data, end=' ')
            self.preorder(root.left)
            self.preorder(root.right)
        return

    def inorder(self, root):
        if root != None:
            self.inorder(root.left)
            print('->', root.data, end=' ')
            self.inorder(root.right)
        return
    
    def postorder(self, root):
        if root != None:
            self.postorder(root.left)
            self.postorder(root.right)
            print('->', root.data, end=' ')
        return
    
myBST = BST()
myBST.insert(14)
myBST.insert(23)
myBST.insert(7)
myBST.insert(10)
myBST.insert(33)
myBST.insert(5)
myBST.insert(20)
myBST.insert(13)
myBST.delete(5)
myBST.delete(33)
myBST.delete(14)
myBST.delete(7)
myBST.delete(23)
myBST.traverse()
myBST.findMin()
myBST.findMax()
