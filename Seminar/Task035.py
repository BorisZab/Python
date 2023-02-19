# Проверка на сложность числа

def difficutal_number(n):
    if n == 2:
        return True
    elif n == 1 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5)):
        if (n % i == 0):
            return False
        return True


print(difficutal_number(int(input())))