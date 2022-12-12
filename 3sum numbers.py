#сумма чисел
if __name__ == '__main__':
    a = int(input())
    sum = 0
    while a != 0:
        sum = sum + a
        a = int(input())
        print(sum)