"""
Підрахувати кількість елементів одновимірного масиву, для яких виконується нерівність i*i<ai<i!
Барбак Владислав Дмитрович 122В
"""
import numpy as np
from math import factorial  # Імпортуємо факторіал з бібліотеки math
while True:
    masive = list(np.array([int(input(f"Введіть число: ")) for i in range(int(input(f"Введіть довжину масиву: ")))]))  # Створюємо масив
    print("Створений масив: ", masive)
    print("Кількість разів виконання рівності (i*i<ai<i!): ", sum(masive.index(a) ** 2 < a < factorial(masive.index(a)) for a in masive))
    result = input("Хочите продовжити? Якщо да - 1, Якщо ні - інше: ")  # Зациклюємо програму
    if result == '1':
        continue
    else:
        break
