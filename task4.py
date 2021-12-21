
# task 4
rent  = float (input ("Введите выручку - "))
cost = float (input("Введите издержку - "))
profit = rent - cost
if profit > 0:
    print (f"Прибыль компании {profit} !")
    print (f"Рентабельность выручки - {profit / rent: 3f}")
    personal = int(input ("Количество сотрудников в компании: - "))
    print (f"Прибыль на одного сотрудника  - { profit/ personal: 2f}")
elif profit <0:
    print (f"Убыток компании - { - profit}")
else:
    print("Покрываете убытки")