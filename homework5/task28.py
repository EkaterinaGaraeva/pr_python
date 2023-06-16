# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
#
# *Пример:*
#
# 2 2
# 4


def sum_of_numbers(num_a: int, num_b: int) -> int:
    if num_b > num_a:
        num_a, num_b = num_b, num_a
    if num_b == 0:
        return num_a
    return sum_of_numbers(num_a + 1, num_b - 1)


a = int(input("Введите число A: "))
b = int(input("Введите число B: "))
print(f"{a} + {b} = {sum_of_numbers(a, b)}")
print(f"Проверка: {a} + {b} = {a+b}")

