"""
Дано два лінійних масиву однакової розмірності. Скласти третій масив з добутку елементів перших двох масивів,
що стоять на місцях з однаковим індексом.
Барбак Владислав Дмитрович 122В
"""
import numpy as np
while True:
    masive_len = int(input("Введіть довжину масивів: "))
    masive1 = np.array([int(input(f"Введіть число 1-го масиву: ")) for i in range(masive_len)]) # Створюємо масиви
    masive2 = np.array([int(input(f"Введіть число 2-го масиву: ")) for i in range(masive_len)])
    print("Перший масив: ", masive1)
    print("Другий масив: ", masive2)
    massive_3 = masive1 * masive2  # Новий масив з добутку двох інших
    print("Третій масив: ", massive_3)
    result = input("Хочите продовжити? Якщо да - 1, Якщо ні - інше: ")  # Зациклюємо програму
    if result == '1':
        continue
    else:
        break