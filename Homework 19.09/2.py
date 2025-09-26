old = int(input('Введите ваш возраст: '))
if old < 18:
    print('Вы "Молодой"')
elif 18 <= old < 60:
    print('Вы "Взрослый"')
elif old >= 60:
    print('Вы "Пожилой"')