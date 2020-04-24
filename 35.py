"""
Дан лінійний масив цілих чисел. Перевірте, чи є він упорядкованим по спаданню.
Барбак Владислав Дмитрович 122В
"""
import numpy as np
while True:
    masive = np.array([int(input(f"Введіть число масиву: ")) for i in range(int(input(f"Введіть довжину масиву: ")))])  # Створюємо масив
    print("Створений масив: ", masive)

    if len(masive) == 1:
        print("Лише одне число!")
    else:
        def bubbleSort(arr):  # Використовуємо бульбашкове сортування
            flag = False
            n = len(arr)
            for i in range(n):
                for j in range(0, n - i - 1):
                    if arr[j] < arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
                        flag = True
                        break
            return flag
        if bubbleSort(masive):
            print("Масив неупорядкований за спаданням")
        else:
            print("Масив упорядкований за спаданням")
        result = input("Хочите продовжити? Якщо да - 1, Якщо ні - інше: ")  # Зациклюємо програму
        if result == '1':
            continue
        else:
            break