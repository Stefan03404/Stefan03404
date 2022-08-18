import math


coll = int(input('Введите кол-во чисел: '))

for num in range(coll):
  number = float(input('Введите число: '))
  if number > 0:
    number = math.ceil(number)
    print('x = ', number, 'log(x) = ', math.log(number))
  elif number < 0:
    number = math.floor(number)
    print('x = ', number, 'exp(x) = ', math.exp(number))
