#task6

while True:
    day = 1
    start_km = float(input('Начальный резкльтат - '))
    target_km  = float(input('Финальный резкльтат -')
    if start_km <= 0 or target_km < 0:
        print('Стартовое значение должно быть больше нуля !=0')
    else:
        while start_km < target_km:
              start_km *= 1.1
              days += 1
    print (f 'Результат будет достигнут за {day} дней')
