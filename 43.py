"""
Задано два натуральних числа a і b. Змінній w привласнити значення істина, якщо в одновимірному цілочисельному масиві
є хоча б один елемент, кратний а і не кратний b.
Барбак Владислав Дмитрович 122В
"""
import numpy as np
while True:
    masive = np.array([int(input(f"Введіть число: ")) for i in range(int(input(f"Введіть довжину масиву: ")))])  # Створюємо масив
    print("Ваш масив: ", masive)
    a, b = int(input("Введіть число a: ")), int(input("Введіть число b: "))
    for i in masive:
        if i % a == 0 and i % b != 0:
            w = True
            print(w)
            break
    result = input("Хочите продовжити? Якщо да - 1, Якщо ні - інше: ")  # Зациклюємо програму
    if result == '1':
        continue
    else:
        break