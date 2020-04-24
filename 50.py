"""
У лотереї розігрувалося 100 квитків. Таблиця містить 10 номерів виграшних квитків. Перевірте, чи є квиток
з номером N виграшним.
Барбак Владислав Дмитрович 122В
"""
import random
while True:
    tickets = list(range(100))
    win_tickets = []
    N = int(input("Введіть номер Вашего квитка: "))
    for i in range(10):
        a = random.choice(tickets)
        win_tickets.append(a)
        tickets.remove(a)  # Виключення повторів
    print(win_tickets)
    if N in win_tickets:
        print("Ви виграли")
    else:
        print("Ви програли")
    result = input("Хочите продовжити? Якщо да - 1, Якщо ні - інше: ")  # Зациклюємо програму
    if result == '1':
        continue
    else:
        break