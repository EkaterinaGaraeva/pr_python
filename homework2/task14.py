# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k),
# не превосходящие числа N.


n = int(input("Введите число N: "))
list_of_num = [2**i for i in range(0, n) if 2**i < n]
print(*list_of_num)

x = 0
list_of_num2 = []
while 2**x < n:
    list_of_num2.append(2**x)
    x += 1
print(*list_of_num2)

