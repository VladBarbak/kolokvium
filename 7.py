"""
Створіть масив А [1..12] за допомогою генератора випадкових чисел з елементами від -20 до 10 і виведіть його на екран.
Замініть всі від’ємні елементи масиву числом 0.
Барбак Владислав Дмитрович 122В
"""
import numpy as np
from random import randint  # Імпортуємо рандом
while True:
    def zero(x):  # Функція перевірки на знак числа
        if x < 0:
            return 0
        else:
            return x
    masive = np.array([randint(-20, 10) for i in range(12)])  # Генеруємо масив рандомних чисел від -20 до 10
    print("Ваш масив: ", masive)
    print("Ваш масив із заміною від'ємних елементів на 0: ", list(map(zero, masive)))  # Проводимо заміну на нуль через функцію zero
    result = input("Хочите продовжити? Якщо да - 1, Якщо ні - інше: ")  # Зациклюємо програму
    if result == '1':
        continue
    else:
        break