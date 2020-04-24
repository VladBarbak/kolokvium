"""
У лінійному масиві знайти максимальний елемент. Вставте порядковий номер елемента за ним, пересунувши всі залишилися
на одну позицію вправо.
Барбак Владислав Дмитрович 122В
"""
import numpy as np
while True:
    masive = list(np.array([int(input("Введіть число: ")) for i in range(int(input("Введіть довжину масиву: ")))])) # Створюємо масив
    print("Ваш масив: ", masive)
    max = max(masive)
    print("Максимальний елемент: ", max)
    masive.insert(masive.index(max) - 1, masive.index(max))  # Перед максимальним число ставимо його індекс
    print("Новый масив: ", masive)
    result = input("Хочите продовжити? Якщо да - 1, Якщо ні - інше: ")  # Зациклюємо програму
    if result == '1':
        continue
    else:
        break