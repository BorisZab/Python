# Заполните массив элементами арифметической прогрессии.
#  Её первый элемент, разность и количество элементов нужно ввести 
# с клавиатуры. Формула для получения n-го члена прогрессии:
# an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
a = int(input())
d = int(input())
n = int(input())
array = []
i = 1
for _ in range(n):
    dif = a+(i-1)*d
    array.append(dif)
    i+=1
print(array)



