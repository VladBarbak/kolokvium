"""
Задано дві таблиці. Одна містить найменування послуг, а інша - розцінкиза ці послуги. Видаліть з обох таблиць все, що
передує послузі, ціна якої G гривень.
Барбак Владислав Дмитрович 122В
"""
while True:
    import numpy as np
    print("Введіть назву послуги та ціну через пробіл")
    table = [] # Пуста таблиця
    while True:
        a = input("Послуга та ціна: ")
        if len(a) == 0:
            break
        table.append(a.split(" "))
    G = input("Введіть ціну для зрізу: ")
    for i in range(len(table)):
        if G in table[i]:
            input_table = table[i:]
            break
    for i in range(len(table)):
        print(f"Послуга: {table[i][0]} Ціна: {int(table[i][1])}")
    result = input("Хочите продовжити? Якщо да - 1, Якщо ні - інше: ")  # Зациклюємо програму
    if result == '1':
        continue
    else:
        break