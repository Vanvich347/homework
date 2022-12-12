#найти треугольник
if __name__ == '__main__':
    a = int(input('numberA'))
    b = int(input('numberB'))
    c = int(input('numberC'))
    if a < b:
        less = a             #меньше
        a = b
        b = less
    if b < c:
        less = b
        b = c
        c = less
    if a >= b + c:
        print('NO')
    elif a * b * c == 0:
        print('NO')
    else:
        print('YES')






