#максимальное растояние между локальными максимумами
if __name__ == '__main__':
    preNumber = int(input())
    number = int(input())
    postNumber = int(input())

    count = 0
    maxCount = 0


    while postNumber != 0:
        if postNumber < number > preNumber:
            if maxCount == 0:
                maxCount = 1
            elif maxCount < count:
                maxCount = count
            count = 1
        count = count + 1
        preNumber = number
        number = postNumber
        postNumber = int(input())


    print(maxCount-2)