#шаг слона
if __name__ == '__main__':
    a = int(input('numberY1')) #расположение слона по Y
    b = int(input('numberX1')) #расположение слона по Х
    c = int(input('numberY2')) #конечная точка по Y
    d = int(input('numberX2')) #конечная точка по X
    if a - c == b - d:
        print('YES')
    elif c - a == d - b:
        print('YES')
    elif a - c == d - b:
        print('YES')
    elif c - a == b - d:
        print('YES')
    else:
        print('NO')
#более правильное
#if __name__ == '__main__':
#    a = int(input())
#    b = int(input())
#    c = int(input())
#    d = int(input())
#    if (c - a) ** 2 == (d - b) ** 2:
#        print('YES')
#    else:
#        print('NO')