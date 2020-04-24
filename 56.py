"""
Якщо в одновимірному масиві є три поспіль однакових елемента, то змінній r привласнити значення істина.
Барбак Владислав Дмитрович 122В
"""
import numpy as np
while True:
    masive = np.array([int(input("Введіть число: ")) for i in range(int(input("Введіть довжину масиву: ")))])  # Створюємо масив
    print("Створений масив: ", masive)
    count = 0  # Лічильник для однакових елементів
    for i in range(len(masive)):
        if masive[i] == masive[i + 1] or masive[i] == masive[i - 1]:
            count += 1
        if count == 3:
            r = True
            print(r)
            break
    result = input("Хочите продовжити? Якщо да - 1, Якщо ні - інше: ")  # Зациклюємо програму
    if result == '1':
        continue
    else:
        break