def degree(a, b):

    if b == 0:
        return 1
    if b <0:
        return degree(a, b+1)*1/b
    return degree(a * a, b - 1)


print(degree(2, 3))