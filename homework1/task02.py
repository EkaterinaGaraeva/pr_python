# Задача 2: Найдите сумму цифр трехзначного числа.
#
# *Пример:*
#
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)


def check_number(num: str, length):
    return True if num.isdigit() and len(num) == length else False

def sum_of_digit_of_three_digit_number(num: int):
    sum_of_digit = 0
    for i in range(3):
        sum_of_digit += num % 10
        num //= 10
    return sum_of_digit

def calculate_sum(num, length):
    print(f"Сумма цифр числа {num} = {sum_of_digit_of_three_digit_number(int(num))}") \
        if check_number(num, length) else print(f"Вы ввели не {length}-значное число")

if __name__ == "__main__":
    number = input("Введите трехзначное число: ")
    calculate_sum(number, 3)

