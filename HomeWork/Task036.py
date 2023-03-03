num_rows = int(input('Write size matix:'))
num_columns = int(input('Write size matix:'))
find= int(input("Write find element: "))
x = 1
mas = [[0] * num_columns for i in range(num_rows)]
for i in range(num_rows):
    for j in range(num_columns):
        mas[i][j] = x
        x += 1
        if mas[i][j]==find:
            print(i, j)  
for i in mas: 
    print(' '.join(list(map(str, i))))
