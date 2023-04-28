class SinglyLinkedList:
    
    def __init__(self):
        self.count = 0
        self.head = None

    def traverse(self):
        print("Traverse: ", end='')
        current_node = self.head
        if current_node == None:
            print("This is an empty list.")
        while current_node != None:
            print(current_node.name, end="")
            current_node = current_node.next
            if current_node != None:
                print(" --> ", end="") 
            else:
                print("")

    def insertFront(self, data):
        pNew = DataNode(data)
        if self.head == None:
            self.head = pNew
        else:
            pNew.next = self.head
            self.head = pNew
        self.count += 1

    def insertLast(self, data):
        pNew = DataNode(data)
        current_node = self.head
        if self.head == None:
            self.head == pNew
        else:
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = pNew
        self.count += 1
    
    def insertBefore(self, node, data):
        pNew = DataNode(data)
        current_node = self.head
        prev_node = self.head
        count = 0
        if self.head.name == node:
            pNew.next = self.head
            self.head = pNew
            self.count += 1
        else:
            while current_node != None:
                if current_node.name == node:
                    break
                current_node = current_node.next
                count += 1
            if current_node == None:
                print("Cannot insert, <node> does not exist.")
            else:
                for _ in range(count-1):
                    prev_node = prev_node.next
                prev_node.next = pNew
                pNew.next = current_node
                self.count += 1
    
    def delete(self, data):
        current_node = self.head
        prev_node = self.head
        count = 0
        if self.head.name == data:
            self.head = current_node.next
            del current_node

        else:
            while current_node != None:
                if current_node.name == data:
                    break
                current_node = current_node.next
                count += 1
            if current_node == None:
                print("Cannot delete, <data> does not exist.")
            else:
                for _ in range(count-1):
                    prev_node = prev_node.next
                prev_node.next = current_node.next
                del current_node
                self.count -= 1
       
class DataNode:
    def __init__(self, person_name=""):
        self.name = person_name
        self.next = None


mylist = SinglyLinkedList()
pNew = DataNode("Rain")
mylist.head = pNew
pNew = DataNode("Phu")
mylist.head.next = pNew
mylist.insertFront("Pare")
mylist.insertLast("Eik")
mylist.insertBefore("Rain", "Mark")
mylist.delete("Frank")
mylist.traverse()