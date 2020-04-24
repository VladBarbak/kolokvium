"""
Обчислити суму парних елементів одновимірного масиву до першого зустрінутого нульового елемента.
Барбак Владислав Дмитрович 122В
"""
import numpy as np
while True:
    masive = list(np.array([int(input(f"Введіть число: ")) for i in range(int(input(f"Введіть довжину масиву: ")))]))  # Створюємо масив
    print("Створений масив: ", masive)
    if 0 in masive:
        masive = masive[:masive.index(0)]
    print("Сума парних елементів до нуля:", sum(filter(lambda x: x % 2 == 0, masive)))  # Виводимо суму парних елементів
    result = input("Хочите продовжити? Якщо да - 1, Якщо ні - інше: ")  # Зациклюємо програму
    if result == '1':
        continue
    else:
        break