n = int(input("Введите число монеток: "))
count_0 = 0
count_1 = 0
import random
for i in range(n):
    k = random.randint(0, 1)
    if k == 0:
        count_0 += 1
    else:
        count_1 += 1
if count_0 <= count_1:
    print(count_0)
else:
    print(count_1)
