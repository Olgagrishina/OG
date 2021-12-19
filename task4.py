# task 4

numbers = []


for i in range(3):
  number = float(input("Введите число #{}: ".format(i + 1)))
  numbers.append(number)

#  наибольшее является первым в списке.
nch = numbers[0]
# сравнение
for number in numbers:
    if number > mayor:
        nch = number
# результат
print("Наибольшее число:", nch)