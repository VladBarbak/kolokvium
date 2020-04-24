"""
Дан одновимірний масив з 10 цілих чисел. Підрахуйте найбільше число однакових чисел, що йдуть підряд в ньому.
Барбак Владислав Дмитрович 122В
"""
import numpy as np
while True:
    masive = np.array([int(input("Введіть число: ")) for i in range(10)])  # Створюємо масив
    print("Створений масив: ", masive)
    count = 1  # Лічильник для послідовностей однакових елементів
    count_final = 0  # Лічильник для найбільшої послідовності однакових чисел
    for i in masive:
        for j in range(1, len(masive)):
            if i == masive[j]:
                count += 1
                if count > count_final:
                    count_final = count
            else:
                count = 0
    print("Найбільше число однакових чисел", count_final)