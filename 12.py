"""
Дані про температуру повітря за декаду грудня зберігаються в масиві. Визначити, скільки раз температура була вище
середньої за цю декаду.
Барбак Владислав Дмитрович 122В
"""
import numpy as np
from random import randint  # Імпортуємо рандом
while True:
    masive = np.array([randint(9, 29) for i in range(10)])  # Генерація масиву
    print("Згенерований масив: ", masive)
    print("Кількість значень які вищі середнього: ", sum(i > masive.mean() for i in masive))  # Виводимо кількість разів коли температура була вища середньої
    result = input("Хочите продовжити? Якщо да - 1, Якщо ні - інше: ")  # Зациклюємо програму
    if result == '1':
        continue
    else:
        break