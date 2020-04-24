"""
Створіть масив з 15 цілочисельних елементів і визначте серед них мінімальне значення.
Барбак Владислав Дмитрович 122В
"""
import numpy as np
from random import randint
while True:
    min = int(input("Введіть мінімальне рандомне значення: "))
    max = int(input("Введіть мінімальне рандомне значення: "))
    masive = np.array([randint(min, max) for i in range(15)])  # Генерація масиву
    print("Згенерований масив: ", masive)
    print("Мінімальне значення: ", masive.min()) # Виведення мінімального значення масиву
    result = input("Хочите продовжити? Якщо да - 1, Якщо ні - інше: ")  # Зациклюємо програму
    if result == '1':
        continue
    else:
        break