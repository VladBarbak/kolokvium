"""
Знайти добуток елементів масиву цілих чисел, які кратні 7. Розмірність масиву - 15. Заповнення масиву здійснити
випадковими числами від 10 до 50.
Барбак Владислав Дмитрович 122В
"""
import numpy as np
from random import randint  # Імпортуємо рандом
while True:
    masive = np.array([randint(10, 50) for i in range(15)])  # Генерація масиву
    print("Згенерований масив: ", masive)
    a = 1
    for i in masive:
        if i % 7 == 0:  # Знаходження чисел кратних 7
            a *= i
    if a != 1:
        print("Добуток чисел кратних 7: ", a)
    else:
        print("Немає чисел, що кратні 7")
    result = input("Хочите продовжити? Якщо да - 1, Якщо ні - інше: ")  # Зациклюємо програму
    if result == '1':
        continue
    else:
        break