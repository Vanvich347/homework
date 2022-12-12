# Куда плыть
if __name__ == '__main__':
    a = int(input('pool langth'))#длинна бассейна
    b = int(input('pool width')) #ширина бассейна
    c = int(input('langht'))     #длинне
    d = int(input('width'))      #ширине
    recto = b - d                #справа
    left = b - recto             #слева
    up = a - c                   #вверх
    down = a - up                #вниз
    if recto < left:
        small = recto            #маленький
        recto = left
        left = small
    if left < up:                #вверх
        small = left
        left = up
        up = small
    if up < down:
        print(up)
    else:
        print(down)



