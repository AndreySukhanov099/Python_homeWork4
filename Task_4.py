#Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
#многочлена и записать в файл многочлен степени k.
#Пример:
#- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
from random import randint
K =int(input("Введите число K "))
a = randint(0, 100)
b = randint(0, 100)
print(f"{a}*x^{K}+{b}*x=0")