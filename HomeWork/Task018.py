# Требуется найти в массиве A[1..N] самый близкий по величине
# элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai.
# Последняя строка содержит число X
import random

n = int(input("Введите колличество элементов: "))
x = int(input("Введите число х:"))
numbers = []
sum = 100
num = 0
min = 0
for i in range(n):
    num = random.randint(0, 9)
    numbers.append(num)
    if abs(x - num) <= sum:
        sum = abs(x - num)
        min = num
print(numbers)
print(min)