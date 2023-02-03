# Найдите сумму цифр трехзначного числа.

n = int(input("Write number: "))
sum = 0
while n:
    sum = sum + n % 10
    n = n // 10
print("Sum numbers:", sum)
