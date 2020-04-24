"""
Знайти кількість парних елементів одновимірного масиву.
Барбак Владислав Дмитрович 122В
"""
import numpy as np
while True:
    masive = np.array([int(input("Введіть елемент масиву: ")) for i in range(int(input("Введіть довжину масиву: ")))])  # Створюємо масив
    print("Створений масив: ", masive)
    print(f"Кількість парних елементів: {sum(((i % 2) == 0) for i in masive)}")
    result = input("Хочите продовжити? Якщо да - 1, Якщо ні - інше: ")  # Зациклюємо програму
    if result == '1':
        continue
    else:
        break