import json

NUMBERS_LIST = '../lists/disordered-numbers-128.json'

steps = 0

def quickSort(arr):
  # TODO: fazer os steps pegarem o real valor de operações (dessa forma n está correta)
  # global steps
  # steps += 1 

  if len(arr) < 2:
    return arr

  middleIndex = len(arr) // 2
  pivot = arr[middleIndex]
  minors = [i for i in arr if i < pivot]
  biggers = [i for i in arr if i > pivot]
  equals = [i for i in arr if i == pivot]

  # print(minors + equals + biggers)

  return quickSort(minors) + equals + quickSort(biggers)

with open(NUMBERS_LIST, 'r') as file:
  data = json.load(file)
  numberList = data['list']

sortedList = quickSort(numberList)

print('Lista organizada: ', sortedList)
# print('Quantidade de passos: ', steps)
