# Задача 12: Петя и Катя – брат и сестра. Петя – студент,
# а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.


import math

def guessed_numbers(sum_of_num, prod_of_num):
    D = sum_of_num**2 - 4 * prod_of_num
    if D > 0:
        x = (sum_of_num + math.sqrt(D))/2
        y = sum_of_num - x
    elif D == 0:
        x = sum_of_num / 2
        y = x
    else:
        x = None
        y = None
    return (x, y)

s = int(input("Введите сумму чисел S = "))
p = int(input("Введите произведение чисел P = "))

x, y = guessed_numbers(s, p)
if x != None and y != None:
    print(f"X = {round(x, 3)}, Y = {round(y, 3)}")
else:
    print("Решения нет")

