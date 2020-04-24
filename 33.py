"""
Заданий масив А (1:20). Знайти добуток всіх його ненульових елементів.
Барбак Владислав Дмитрович 122В
"""
import numpy as np
while True:
    masive = np.array([int(input(f"Введіть число: ")) for i in range(1, 21)])  # Створюємо масив
    print("Створений масив: ", masive)
    prod = 1
    for i in masive:  # Пошук ненульових елементів
        if i != 0:
            prod *= i
    if prod == 1:
        print("У масиві лише нулі або одиниці")
    else:
        print(f"Добуток ненульових чисел масиву = {prod}")
    result = input("Хочите продовжити? Якщо да - 1, Якщо ні - інше: ")  # Зациклюємо програму
    if result == '1':
        continue
    else:
        break