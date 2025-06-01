import json

NAMES_LIST = '../lists/128-ordened-names-list.json'

def binarySearch(list, item):
  low = 0
  high = len(list) - 1
  steps = 0

  while low <= high:
    middle = (low + high) // 2 
    guess = list[middle]
    # print(middle)

    if guess == item:
      steps = steps + 1
      print(f"Passos dados: {steps}")
      return middle
    if guess > item:
      steps = steps + 1
      high = middle - 1
    else:
      steps = steps + 1
      low = middle + 1

  print(f"Passos dados: {steps}")
  return -1

with open(NAMES_LIST, 'r', encoding='utf-8') as file:
  data = json.load(file)

names = data['names']
target = input('Nome: ')
index = binarySearch(names, target)

if index == -1:
  print('Nome não listado.')
  exit()

print(f"O nome {names[index]} foi encontrado no index {index}!")
