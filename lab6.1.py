import math as m
import numpy
a = float(input('Введіть нижню границю: '))
b = float(input('Введіть верхню границю: '))
h = float(input('Введіть значення кроку: '))
for bar in numpy.arange(a, b+h):
    print(3 - m.log(m.fabs(bar - 6), m.e) + m.cos(bar))