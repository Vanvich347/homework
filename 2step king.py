#шаг короля
if __name__ == '__main__':
    a = int(input('numberY1'))
    b = int(input('numberX1'))
    c = int(input('numberY2'))
    d = int(input('numberX2'))
if c == a and d == b + 1:
    print('YES')
elif c == a and d == b - 1:
    print('YES')
elif c == a and d == b:
    print('YES')
elif c == a + 1 and d == b:
    print('YES')
elif c == a - 1 and d == b:
    print('YES')
elif c == a - 1 and d == b - 1:
    print('YES')
elif c == a + 1 and d == b + 1:
    print('YES')
else:
    print('NO')


