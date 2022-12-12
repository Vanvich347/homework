if __name__ == '__main__':
    number = int(input('check number'))
    number4 = number % 10
    number3 = number % 100 // 10
    number2 = number % 1000 // 100
    number1 = number // 1000
    number41 = (number4 // (number1+1))-1
    number32 = (number3 // (number2+1))-1
    res = number41 * number32
    print(res)


