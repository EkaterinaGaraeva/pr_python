# Задача 6: Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
#
# *Пример:*
#
# 385916 -> yes
# 123456 -> no


from task02 import check_number
from task02 import sum_of_digit_of_three_digit_number

def lucky_ticket(num, length):
    num1, num2 = int(num) // 1000, int(num) % 1000 if check_number(number, length) else print("Неверный номер билета")
    sum1, sum2 = sum_of_digit_of_three_digit_number(num1), sum_of_digit_of_three_digit_number(num2)
    return f"{num} -> yes" if sum1 == sum2 else f"{num} -> no"

number = input("Введите номер билета: ")
print(lucky_ticket(number, 6))

