"""
Знайти добуток всіх елементів масиву цілих чисел, менших 0. Розмірність масиву - 10. Заповнення масиву здійснити
за допомогою клавіатури.
Барбак Владислав Дмитрович 122В
"""
import numpy as np
while True:
    masive = np.array([int(input("Введіть ціле число: ")) for i in range(10)])  # Створення масиву
    print("Згенерований масив: ", masive)
    a = 1
    for i in masive:  # Перевірка на чисело менше 0
        if i < 0:
            a *= i
    if a != 1:
        print("Добуток елементів: ", a)
    else:
        print("Елементів що менше 0 немає")
    result = input("Хочите продовжити? Якщо да - 1, Якщо ні - інше: ")  # Зациклюємо програму
    if result == '1':
        continue
    else:
        break