if __name__ == '__main__':
    a = int(input('hours of first moment'))
    b = int(input('minutes of first moment'))
    c = int(input('seconds of first moment'))
    d = int(input('hours of second moment'))
    e = int(input('minutes of second moment'))
    f = int(input('seconds of second moment'))
    first = a * 3600 + b * 60 + c
    second = d * 3600 + e * 60 + f
    time = second - first
    hours = time // 3600
    minutes = time % 3600 // 60
    seconds = time % 3600 % 60
    print(hours)
    print(minutes)
    print(seconds)