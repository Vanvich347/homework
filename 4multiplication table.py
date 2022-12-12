#таблица умножения
if __name__ == '__main__':
    i = 1
    while i <= 9:
        one = i
        two = i + i
        three = two + i
        four = three + i
        five = four + i
        six = five + i
        seven = six + i
        eight = seven + i
        nine = eight + i
        i = i + 1
        print(one,two,three,four,five,six,seven,eight,nine)
# проще правиьно
if __name__ == '__main__':
    for i in range(1, 11):
        for j in range(1, 11):
            print((i * j), end="\t")
        print('\n')