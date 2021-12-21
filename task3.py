n = int(input("Введите положительное число n: "))
temp = str(n)
p1 = temp + temp
p2 = temp + temp + temp
result = n + int(p1) + int(p2)
print("Результат равен:", result)
