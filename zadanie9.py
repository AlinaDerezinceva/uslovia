shotrange = float(input('введите дальность выстрела: '))

if shotrange > 28 and shotrange < 30:
    print('Попал')
elif shotrange >= 30:
    print('Перелет')
elif shotrange > 0 and shotrange <= 28:
    print('Недолет')
elif shotrange <=0:
    print('Не бей по своим')