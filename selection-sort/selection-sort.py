import json

NUMBERS_LIST = '../lists/50-disordered-numbers.json'

steps = 0

def selection_sort(arr):
    global steps
    
    for i in range(len(arr)):
        minIndex = i

        for j in range(i + 1, len(arr)):
            steps += 1
            if arr[j] < arr[minIndex]:
                minIndex = j
        
        arr[i], arr[minIndex] = arr[minIndex], arr[i]

        # print(f"Passo {i + 1}: {arr}")
    return arr

with open(NUMBERS_LIST, 'r') as file:
    data = json.load(file)
    numbersList = data['list']

selection_sort(numbersList)

print("Lista ordenada:", numbersList)
print("Quantidade de passos: ", steps)
