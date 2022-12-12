#показать наибольшее число
if __name__ == '__main__':
    a = int(input('number1'))
    b = int(input('number2'))
    c = int(input('number3'))
    if a > b:
        more = a             #больше
        a = b
        b = more
    if b > c:
        more = b
        b = c
        c = more
    print(c)






