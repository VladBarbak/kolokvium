"""
Відомість на зарплату представлена як дві таблиці. Одна міститьпрізвища працівників цеху, а друга - їх зарплату за
поточний місяць. Знайдіть прізвище працівника, зарплата якого найменш відхиляється від середньої зарплати всіх
працівників за поточний місяць. Знайдіть прізвища двох працівників з найбільшою заробітною платою. Видаліть з відомості
на зарплату відомості про працівника, зарплата якого мінімальна.
Барбак Владислав Дмитрович 122В
"""
import numpy as np
while True:
    length = int(input('Введіть кіклькість працівників: '))
    workers = [input("Прізвище працівника: ") for i in range(length)]
    workers2 = workers[:]  # Використовується для видалень
    payment = [int(input("Заробітня плата: ")) for i in range(length)]
    payment2 = payment[:]
    average_payment = np.array(payment).mean()
    print(min(payment, key=lambda num: abs(num - average_payment)))
    for i in range(2):
        max_pay = max(payment)
        max_worker = workers[payment.index(max_pay)]  # Знаходимо ідентичний індекс зарплатні у списку робітників
        print(f"Найбільша зарплата {max_pay}грн. у {max_worker}")
        workers.remove(max_worker)
        payment.remove(max_pay)
    print(f"Зі списку видалено невдаху {workers2[payment2.index(min(payment2))]} із зарплатнею {min(payment2)}грн.")
    print("Список працівників та їх заробітніх плат:")
    for i in range(len(payment2)):
        print(f"{workers2[i]} - {payment2[i]}")
    result = input("Хочите продовжити? Якщо да - 1, Якщо ні - інше: ")  # Зациклюємо програму
    if result == '1':
        continue
    else:
        break