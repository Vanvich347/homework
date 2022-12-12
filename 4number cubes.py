#кубы чисел
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    for i in range(a,b + 1):
        cube = i * i * i
        print(cube)