"""
Перетин даху має форму півкола з радіусом R м. Сформувати таблицю, яка містить довжини опор, які встановлюються
через кожні R / 5 м.
Барбак Владислав Дмитрович 122В
"""
import math
while True:
    radius = int(input('Введіть радіус: '))
    distance = radius / 5
    x = 0
    i = 0
    while x < 2 * radius - distance:
        x += distance
        i += 1
        print(f'{i} опора =', math.sqrt(x * (2 * radius - x)))
    result = input("Хочите продовжити? Якщо да - 1, Якщо ні - інше: ")  # Зациклюємо програму
    if result == '1':
        continue
    else:
        break