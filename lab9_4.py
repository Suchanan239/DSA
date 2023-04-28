def insertionSort(list, last):
    compare = 0
    current = 1
    while (current <= last):
        hold = list[current]
        walker = current-1
        compare += 1
        while (walker >= 0 and  deck(hold) < deck(list[walker])):
            list[walker+1] = list[walker]
            walker -= 1
            compare += 1
        list[walker+1] = hold
        current += 1
        if walker < 0:
            compare -= 1
        print(list)
    print("comparison times:", compare)

def selectionSort(list, last):
    current = 0
    compare = 0
    while current < last:
        smallest = current
        walker = current+1
        while walker <= last:
            compare += 1
            if deck(list[walker]) < deck(list[smallest]):
                smallest = walker
            walker += 1
        list[current] , list[smallest ]= list[smallest], list[current]
        current += 1
        print(list)
    print("Comparison times:", compare)

def bubbleSort(list, last):
    current = 0
    compare = 0
    sorted = False
    while current <= last and sorted == False:
        walker = last
        sorted = True
        while walker > current:
            compare += 1
            if deck(list[walker]) < deck(list[walker-1]):
                sorted = False
                list[walker], list[walker-1] = list[walker-1], list[walker]
            walker -= 1
        current += 1
        print(list)
    print("Comparison times:", compare)

def deck(list):
    number_of_card = {"2" :1, "3" :2, "4" :3, "5" :4, "6" :5, "7" :6, "8" :7, "9" :8, \
                      "10" :9, "J" :10, "Q" :11, "K" :12, "A" :13}
    sign = {"♣" :1, "♦" :2, "♥" :3, "♠" :4}
    list_of_card = (number_of_card[list[:-1]], sign[list[-1]])
    return list_of_card

# insertionSort(['4♣', 'A♣', '10♥', 'K♦', '4♠', '10♣', '3♦', '7♥', '4♦'], 8)
# selectionSort(['4♣', 'A♣', '10♥', 'K♦', '4♠', '10♣', '3♦', '7♥', '4♦'], 8)
bubbleSort(['4♣', 'A♣', '10♥', 'K♦', '4♠', '10♣', '3♦', '7♥', '4♦'], 8)