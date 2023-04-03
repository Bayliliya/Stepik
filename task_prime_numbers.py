'''Нахождение всех простых чисел от a до b включительно'''


a_num = int(input("Введите число a: "))
b_num = int(input("Введите число b: "))

flag_prime = 0

if a_num == 1:
    a_num = a_num + 1

for i in range(a_num, b_num + 1):
    for j in range(2, b_num):
        if i % j == 0 and i != j:
            flag_prime = 1
    if flag_prime == 0:
        print(i)
    else:
        flag_prime = 0
