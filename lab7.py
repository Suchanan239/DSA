from time import time
import random

def summation(num):
    sum = 0
    for i in range(1, num+1):
        sum += i
    
    # sum = (num/2)*(num+1)
    
    return sum

def randomList(num):
    a_list = list(random.sample(range(1, 100000000), num))
    b_list = list(random.sample(range(100000001, 200000000), num))
    c_list = list(random.sample(range(200000001, 300000000), num))
    return a_list, b_list, c_list

def isintersec(a_list, b_list, c_list):
    for  i in a_list:
        if i in b_list and i in c_list: #this is O(n^2)
            return True
    return False
        

def isintersec_n2(a_list, b_list, c_list): #this is O(n^2)/wrong
    for i in a_list:
        if i in b_list: #if i in .... worst case is n so it's kinda like another for loop but not axactly so in this case it's more than O(n^2) but not O(n^3)
            for j in c_list:
                if j == i:
                    return True
    return False
        
def isintersec_n3(a_list, b_list, c_list): #this is O(n^3)
    for i in a_list:
        for j in b_list:
                for k in c_list:
                    if i == j == k:
                        return True
    return False


def analyze_algo(num):
    # stime = time()
    # summation(num)
    # etime = time()
    # elapsed = etime - stime
    # print("execution time: %f" %elapsed)
    a_list, b_list, c_list = randomList(num)
    stime = time()
    # isintersec(a_list, b_list, c_list)
    # isintersec_n2(a_list, b_list, c_list)
    isintersec_n3(a_list, b_list, c_list)
    etime = time()
    elapsed = etime - stime
    print("execution time: %f" %elapsed)
    # print(isintersec(a_list, b_list, c_list))
    # print(isintersec_n2(a_list, b_list, c_list))
    print(isintersec_n3(a_list, b_list, c_list))

analyze_algo(10000)
# print(isintersec([50, 20, 40], [10, 80, 20], [20, 60, 90]))
# print(isintersec_n2([50, 20, 40], [10, 80, 20], [20, 60, 90]))
# print(isintersec_n3([50, 20, 40], [10, 80, 20], [20, 60, 90]))