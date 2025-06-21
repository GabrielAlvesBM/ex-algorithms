number1 = int(input('Número 1: '))
number2 = int(input('Número 2: '))

def recursiveMdc(number1: int, number2: int) -> int:
  temp = number1 % number2
  if (temp == 0):
    return number2
  
  return recursiveMdc(number2, temp)

def mdc(number1: int, number2: int) -> int:
  while number1 % number2 != 0:
    divider = number1 % number2
    number1, number2 = number2, divider

  return number2

result = mdc(number1, number2)

print(f'MDC de {number1} e {number2} é {result}')