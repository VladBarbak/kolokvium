"""
Створіть масив А [1..8] за допомогою генератора випадкових чисел з елементами від -10 до 10 і виведіть його на екран.
Підрахуйте кількість від’ємних елементів масиву.
Барбак Владислав Дмитрович 122В
"""
import numpy as np
from random import randint  # Імпортуємо рандом
while True:
    masive = np.array([randint(-10, 10) for i in range(8)])  # Генеруємо масив
    print("Згенерований масив: ", masive)  # Виводимо масив
    print("Кількість елементів що менше 0: ", sum(i < 0 for i in masive))  # Виводимо кількість елементів що менше 0
    result = input("Хочите продовжити? Якщо да - 1, Якщо ні - інше: ")  # Зациклюємо програму
    if result == '1':
        continue
    else:
        break