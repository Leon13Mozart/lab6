import math as m
a = float(input('Введіть нижню границю: '))
b = float(input('Введіть верхню границю: '))
h = float(input('Введіть значення кроку: '))
while a <= b:
    print(3 - m.log(m.fabs(a - 6), m.e) + m.cos(a))
    a += h