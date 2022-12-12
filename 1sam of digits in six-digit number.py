if __name__ == '__main__':
    number = int(input('Число'))
    a = number % 10
    b = number % 100 // 10
    c = number % 1000 // 100
    d = number % 10000 // 1000
    e = number % 100000 // 10000
    f = number // 100000
    res = a+b+c+d+e+f
    print(res)
    
