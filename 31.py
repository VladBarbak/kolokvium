"""
Обчислити середнє арифметичне значення тих елементів одновимірного масиву, які потрапляють в інтервал від -2 до 10.
Барбак Владислав Дмитрович 122В
"""
import numpy as np
while True:
    masive = list(np.array([int(input(f"Введіть число: ")) for i in range(int(input("Введіть довжину масиву: ")))]))  # Створюємо масив
    print("Створений масив: ", masive)
    for i in masive:  # Проходим по елементах та видаляємо ті які не належать інтервалу
        if i not in range(-2, 11):
            masive.remove(i)
    print(f"Новий масив: {np.array(masive)}\n"
          f"Середнє арифметичне значення елементів: {np.array(masive).mean()}")
    result = input("Хочите продовжити? Якщо да - 1, Якщо ні - інше: ")  # Зациклюємо програму
    if result == '1':
        continue
    else:
        break