"""
Знайти добуток елементів масиву, кратних 3 і 9. Розмірність масиву - 10. Заповнення масиву здійснити випадковими
числами від 5 до 500.
Барбак Владислав Дмитрович 122В
"""
import numpy as np
from random import randint  # Імпортуємо рандом
while True:
    masive = np.array([randint(5, 500) for i in range(10)])  # Генерація масиву
    print("Згенерований масив: ", masive)
    prod = 1
    for i in masive:
        if i % 3 == 0 and i % 9 == 0:  # Пошук елементів що кратні 3 і 9
            prod *= i
    if prod != 1:
        print("Добуток елементів: ", prod)
    else:
        print("Таких елементів НЕМАЄ")
    result = input("Хочите продовжити? Якщо да - 1, Якщо ні - інше: ")  # Зациклюємо програму
    if result == '1':
        continue
    else:
        break