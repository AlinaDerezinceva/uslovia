x = int(input('x: '))
y = int(input('y: '))
z = int(input('z: '))

if x < y+z and y < x+z and z < x+y:
    print('существует')
else:
    print('не существует')