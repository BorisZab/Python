import math

sum = int(input("Введите сумму:"))
com = int(input("Введите произведение:"))
x = int(
    math.sqrt(((sum * (-1)) + math.sqrt(sum * sum - 4 * com)) / 2 *
              ((sum * (-1)) + math.sqrt(sum * sum - 4 * com)) / 2))
y = int(
    math.sqrt(((sum * (-1)) - math.sqrt(sum * sum - 4 * com)) / 2 *
              ((sum * (-1)) - math.sqrt(sum * sum - 4 * com)) / 2))
print(x, y)
