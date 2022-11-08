import math as m
a = float(input('Введіть нижню границю: '))
b = float(input('Введіть верхню границю: '))
h = float(input('Введіть значення кроку: '))
spisok = []
while a <= b:
    spisok.append(3 - m.log(m.fabs(a - 6), m.e) + m.cos(a))
    a += h
print(spisok)
foo = 0
while foo != len(spisok):
    print(spisok[foo])
    foo += 1
