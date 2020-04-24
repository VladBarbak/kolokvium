"""
Дані про температуру повітря і кількості опадів за декаду квітня зберігаються в масивах. Визначити кількість опадів,
що випали у вигляді дощу і у вигляді снігу за цю декаду.
Барбак Владислав Дмитрович 122В
"""
import numpy as np
from random import randint  # Імпортуємо рандом
while True:
    masive_temp = np.array([randint(-42, 42) for i in range(10)]) # Створюємо масиви
    masive_opadu = np.array([randint(2, 5) for i in range(10)])
    print(f"Масив температур повітря: {masive_temp}\n"
          f""f"Масив опадів: {masive_opadu}")
    rain = 0
    snow = 0
    count = 0
    for i in masive_temp:
        if i <= 0:
            snow += masive_opadu[count]
        else:
            rain += masive_opadu[count]
        count += 1
    print(f"Кількть дощу {rain}мм\n"
          f"Кількість снігу {snow}мм")
    result = input("Хочите продовжити? Якщо да - 1, Якщо ні - інше: ")  # Зациклюємо програму
    if result == '1':
        continue
    else:
        break