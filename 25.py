"""
Знайти добуток елементів лінійного масиву цілих чисел, які кратні 5. Розмірність масиву - 10. Заповнення масиву
здійснити випадковими числами від 10 до 100.
Барбак Владислав Дмитрович 122В
"""
import numpy as np
from random import randint  # Імпортуємо рандом
while True:
    masive = np.array([randint(10, 100) for i in range(10)])  # Генерація масиву
    print("Ваш масив: ", masive)
    prod = 1
    for i in masive:  # Пошук елементів що кратні 5
        if i % 5 == 0:
            prod *= i
    if prod != 1:
        print("Добуток елементів: ", prod)
    else:
        print("Елементів що кратні 5 немає")
    result = input("Хочите продовжити? Якщо да - 1, Якщо ні - інше: ")  # Зациклюємо програму
    if result == '1':
        continue
    else:
        break