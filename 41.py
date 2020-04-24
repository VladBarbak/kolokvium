"""
Змінній t привласнити значення істина, якщо максимальний елемент одновимірного масиву єдиний і не перевищує наперед
заданого числа а.
Барбак Владислав Дмитрович 122В
"""
import numpy as np
from collections import Counter  # Підрахунок елементів
while True:
    masive = np.array([int(input(f"Введіть число: ")) for i in range(int(input(f"Введіть довжину масиву: ")))])  # Створюємо масив
    a = int(input("Введіть число, з ким буде порівнюватись максимальний елемент: "))
    print("Створений масив: ", masive)
    counter = Counter(masive)
    max = masive.max()
    if counter[max] == 1 and max <= a:
        t = True
        print(t)
    else:
        print(False)
    result = input("Хочите продовжити? Якщо да - 1, Якщо ні - інше: ")  # Зациклюємо програму
    if result == '1':
        continue
    else:
        break