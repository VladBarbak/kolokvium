"""
Дан одновимірний масив з 10 цілих чисел. Підрахуйте кількість різних чисел в ньому.
Барбак Владислав Дмитрович 122В
"""
import numpy as np
while True:
    masive = np.array([int(input("Введіть число: ")) for i in range(10)])  # Створюємо масив
    print("Створений масив: ", masive)
    print("Кількість різних чисел: ", len(set(masive)))
    result = input("Хочите продовжити? Якщо да - 1, Якщо ні - інше: ")  # Зациклюємо програму
    if result == '1':
        continue
    else:
        break