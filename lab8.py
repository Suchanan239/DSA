class ProbHash:
    def __init__(self, cap):
        self.hashtable = cap*[None]
        self.n = cap

    def hashFunction(self, mykey):
        return mykey % self.n
    
    def rehashFunction(self, hashkey):
        return (hashkey+1) % self.n
    
    def insertData(self, student_obj):
        index = self.hashFunction(student_obj.getId())
        
        while True:
            if self.hashtable[index] == None:
                self.hashtable[index] = student_obj
                print("insert", student_obj.getId(), "at index", index)
                break
            else:
                index = self.rehashFunction(index)
            # if index > self.n:
            #     print("cannot insert")
            #     break
        return
    
    def searchData(self, key):
        index = self.hashFunction(key)
        while True:
            if self.hashtable[index] != None:
                if self.hashtable[index].getId() == key:
                    print("Found", key, "at index", index)
                    return self.hashtable[index]
                    
                else:
                    index = self.rehashFunction(index)
            else:
                print(key, "does not exist.")
                break

    
class Student:
    def __init__(self, id, name, gpa):
        self.id = id
        self.name = name
        self.gpa = gpa

    def getId(self):
        return self.id
    
    def getName(self):
        return self.name
    
    def getGpa(self):
        return self.gpa
    
    def printDetail(self):
        print("ID:", self.getId())
        print("Name:", self.getName())
        print("GPA:", self.getGpa())
        return
            
s1 = Student(65070001, "Sandee Boonmak", 3.05)
s2 = Student(65070077, "Somsak Jaidee", 2.78)
s3 = Student(65070021, "Somsri Jaiyai", 3.44)
s4 = Student(65070042, "Sommai Meeboon", 2.89)

myHash = ProbHash(3)
myHash.insertData(s1)
myHash.insertData(s2)
myHash.insertData(s3)
myHash.insertData(s4)

std = myHash.searchData(65070077)
std.printDetail()
print("----------------")
std = myHash.searchData(65070021)
std.printDetail()
print("----------------")
std = myHash.searchData(65070042)
std.printDetail()
print("----------------")
std = myHash.searchData(65070032)
