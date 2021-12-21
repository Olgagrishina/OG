# task 4
num_init = int(input('Введите целое положительное число - '))
max =num_init % 10
numb = num_init

while numb > 0:
    digit = numb % 10
    if digit > max:
        max = digit

    if digit == 9
        break
    numb // = 10
    print (numb)


print ("Наибольшая цифра в числе {num_init} равна {max}")

