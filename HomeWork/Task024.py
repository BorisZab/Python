import random

n = int(input("Введите колличество кустов: "))
list = []
for i in range(n):
    f = random.randint(1, 9)
    list.append(f)
max_sum = 0
i = 0
while i <= n:
    sum = list[n - 1 - i] + list[n - 2 - i] + list[n - 3 - i]
    if sum > max_sum:
        max_sum = sum
    i += 1
print(list, max_sum)