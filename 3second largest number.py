# второе по величине число
if __name__ == '__main__':
    a = int(input())
    maximum = a
    while a != 0:
        if maximum < a:
            minimum = maximum
            maximum = a
        a = int(input())
    print(minimum)
    # разбирали на уроке
    if __name__ == '__main__':
        a = int(input('number'))
        b = int(input('number'))
        max = 0
        preMax = 0
        if a > b:
            max = a
            preMax = b
        else:
            preMax = a
            max = b
        while a != 0:
            if a > max:
                preMax = max
                max = a
            if max > a > preMax:
                preMax = a
            a = int(input('number'))
        print(preMax)
