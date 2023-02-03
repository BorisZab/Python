# Требуется вычислить, сколько раз встречается некоторое число X
# в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai.
# Последняя строка содержит число X

# n = int(input("Введите колличество элементов: "))
# x =  int(input("Введите иcкомое число: "))
# count = 0
# for _ in range(n):
#     a = int(input())
#     if a == x:
#         count+=1
# print(count)
import os

clear = lambda: os.system('clear')

n = int(input("Введите колличество элементов: "))
f = int(input("Введите иcкомое число: "))
numbers = []
count = 0
for i in range(n):
    x = int(input())
    numbers.append(x)
    if x == f:
        count += 1
clear()
print(n)
print(numbers)
print(f)
print(count)