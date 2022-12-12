#факториал чисел
if __name__ == '__main__':
    b = int(input())
    for i in range(1,b + 1):
        factorial = i * (i + 1)
        print(factorial)
#правильное решение
if __name__ == '__main__':
    fact_num = int(input())
    multi = 1
    for i in range(1, fact_num + 1):
        multi = multi * i
    print(multi)