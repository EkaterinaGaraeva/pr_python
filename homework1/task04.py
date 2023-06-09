# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок,
# если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
#
# *Пример:*
#
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10


def number_of_cranes(count):
    return int(count / 6)

S = int(input("Введите общее количество журавликов: "))
print(f"Петя - {number_of_cranes(S)}, Катя - {4 * number_of_cranes(S)}, Сережа - {number_of_cranes(S)}") \
    if S % 6 == 0 else print("Некорректное число")

