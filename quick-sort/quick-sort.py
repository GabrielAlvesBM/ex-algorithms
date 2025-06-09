import json

NUMBERS_LIST = '../lists/disordered-numbers-128.json'

steps = {
    'recursive_calls': 0,
    'comparisons': 0
}

def quickSort(arr):
  steps['recursive_calls'] += 1

  if len(arr) < 2:
    return arr

  middleIndex = len(arr) // 2
  pivot = arr[middleIndex]
  minors = []
  biggers = []
  equals = []

  for i in arr:
    steps['comparisons'] += 1

    if i < pivot:
      minors.append(i)
    elif i > pivot:
      biggers.append(i)
    else:
      equals.append(i)

  return quickSort(minors) + equals + quickSort(biggers)

with open(NUMBERS_LIST, 'r') as file:
  data = json.load(file)
  numberList = data['list']

sortedList = quickSort(numberList)

print('Lista organizada: ', sortedList)
print('Chamadas recursivas: ', steps['recursive_calls'])
print('Comparações: ', steps['comparisons'])
print('Quantidade total de passos: ', steps['recursive_calls'] + steps['comparisons'])
