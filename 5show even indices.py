#показать чётные индексы
if __name__ == '__main__':
    a = []
    b = int(input('how many'))
    for i in range(b):
        a.append(int(input('elements')))
    print(a[::2])



