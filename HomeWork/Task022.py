n = int(input("Введите количество элементов первого множества: "))
m = int(input("Введите количество элементов вторго множества:"))
num_1 = set()
num_2 = set()
print("Вводите значения первого множества:")
for i in range(n):
    f = int(input())
    num_1.add(f)
print("Вводите значения второго множества:")
for i in range(m):
    f = int(input())
    num_2.add(f)
result = num_1.intersection(num_2)
print(result)
