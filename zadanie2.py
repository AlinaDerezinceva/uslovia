x = int(input('Введите первое число: '))
y = int(input('Введите второе число: '))
z = int(input('Введите третье число: '))

if (x > y and x < z) or (x > z and x < y):
        print(x)
elif (y > x and y < z) or (y > z and y < x):
        print(y)
elif (z > x and z < y) or (z > y and z < x):
        print(z)
elif x == y or x == z or y == z:
        print('ошибка')