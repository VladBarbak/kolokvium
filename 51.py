"""
Дан одновимірний масив а. Сформувати новий масив, який складається тільки з тих елементів масиву а, які перевищують
свій номер на 10. Якщо таких елементів немає, то видати повідомлення.
Барбак Владислав Дмитрович 122В
"""
import numpy as np
while True:
    masive = np.array([int(input("Введіть елемент: ")) for i in range(int(input("Введіть кількість елементів: ")))])  # Створюємо масив
    print("Створений масив: ", masive)
    future_massive = []
    index_count = 0
    for i in masive:
        if i - index_count == 10:  # Перевірка на індекс
            future_massive.append(i)
        index_count += 1
    if len(future_massive) > 0:
        print("Новий масив: ", np.array(future_massive))
    else:
        print("Немає елементів масиву що задовільняють умову")
    result = input("Хочите продовжити? Якщо да - 1, Якщо ні - інше: ")  # Зациклюємо програму
    if result == '1':
        continue
    else:
        break