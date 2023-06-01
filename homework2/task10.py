# Задача 10: На столе лежат n монеток.
# Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть


import random

def min_count_of_coins(num, coins):
    sum_of_coins = sum(coins)
    return sum_of_coins if sum_of_coins <= (num - sum_of_coins) else num - sum_of_coins

n = int(input("Введите количество монеток: "))
list_of_coins = [random.randint(0, 1) for i in range(0, n)]
print(list_of_coins)
print(f"Минимальное количество монет, которые нужно перевернуть = {min_count_of_coins(n, list_of_coins)}")

