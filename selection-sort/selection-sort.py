import json

NUMBERS_LIST = '../lists/50-disordered-numbers.json'

def selection_sort(arr):
    length = len(arr)
    
    for i in range(length):
        minIndex = i

        for j in range(i + 1, length):
            if arr[j] < arr[minIndex]:
                minIndex = j
        
        arr[i], arr[minIndex] = arr[minIndex], arr[i]

        # print(f"Passo {i + 1}: {arr}")
    return arr

with open(NUMBERS_LIST, 'r') as file:
    data = json.load(file)
    numbersList = data['list']

selection_sort(numbersList)

print("\nLista ordenada:", numbersList)
