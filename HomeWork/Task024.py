import random

n = int(input("Введите колличество кустов: "))
list = []
for i in range(n):
    f = random.randint(1, 9)
    list.append(f)
max_sum = 0
count = 0
i = 0
while count <= n:
    sum = list[len(list) - 1 - i] + list[len(list) - 2 - i] + list[len(list) -
                                                                   3 - i]
    if sum > max_sum:
        max_sum = sum
    count += 1
    i += 1
print(list, max_sum)