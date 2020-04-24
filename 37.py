"""
Розсортуйте заданий лінійний масив по зростанню.
Барбак Владислав Дмитрович 122В
"""
import numpy as np
while True:
    masive = np.array([int(input(f"Введіть число масиву: ")) for i in range(int(input(f"Введіть довжину масиву: ")))])  # Створюємо масив
    print("Створений масив: ", masive)
    def bubbleSort(arr):  # Використовуємо бульбашкове сортування
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr
    print("Сортування бульбашковим методом за зростанням: ", bubbleSort(masive))
    result = input("Хочите продовжити? Якщо да - 1, Якщо ні - інше: ")  # Зациклюємо програму
    if result == '1':
        continue
    else:
        break
