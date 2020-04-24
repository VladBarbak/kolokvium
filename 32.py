"""
Змінній t привласнити значення істина, якщо в одновимірному масиві є хоча б одне від’ємне і парне число..
Барбак Владислав Дмитрович 122В
"""
import numpy as np
while True:
    masive = np.array([int(input(f"Введіть число: ")) for i in range(int(input("Введіть довжину масиву: ")))])  # Створюємо масив
    print("Створений масив: ", masive)
    flag_1 = False  # Прапори необхідня для перевірки умов
    flag_2 = False
    for i in masive:
        if i % 2 == 0:
            flag_1 = True
        if i < 0:
            flag_2 = True
        if flag_1 and flag_2:
            t = True
            print(t)
            break
    else:
        print("Умови не виконані")
    result = input("Хочите продовжити? Якщо да - 1, Якщо ні - інше: ")  # Зациклюємо програму
    if result == '1':
        continue
    else:
        break