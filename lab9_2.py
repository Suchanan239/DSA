def selectionSort(list, last):
    current = 0
    compare = 0
    while current < last:
        smallest = current
        walker = current+1
        while walker <= last:
            compare += 1
            if list[walker] < list[smallest]:
                smallest = walker
            walker += 1
        list[current] , list[smallest ]= list[smallest], list[current]
        current += 1
        print(list)
    print("Comparison times:", compare)

selectionSort([23, 78, 45, 8, 32, 56], 5)