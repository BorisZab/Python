# Определить индексы элементов массива (списка),
#  значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного
#  максимума)
# -5 9 0 3 -1 -2 1 4 -2 10 2 0 -9 8 10 -9 0 -5 -5 7
# 5
# 15
# [1, 9, 13, 14, 19]

array = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min = int(input())
max = int(input())
index = []
j = 0
for i in array:
    if i >= min and i <= max:
        index.append(j)
    j += 1
print(index)

print([ind for ind, val in enumerate(array)if min <= val <= max])