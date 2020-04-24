"""
Знайти найбільший елемент з елементів одновимірного масиву, що мають парний номер. Визначити, чи є він єдиним.
Барбак Владислав Дмитрович 122В
"""
import numpy as np
while True:
    masive = np.array([int(input("Введіть елемент: ")) for i in range(int(input("Введіть кількість елементів: ")))])  # Створюємо масив
    print("Створений масив: ", masive)
    list = [masive[i] for i in range(0, len(masive), 2)]  # Список з парними індеками
    max = max(list)
    if list.count(max) == 1:
        print("Максимальний елемент єдиний")
    else:
        print("Максимальний елемент не єдиний")
    result = input("Хочите продовжити? Якщо да - 1, Якщо ні - інше: ")  # Зациклюємо програму
    if result == '1':
        continue
    else:
        break