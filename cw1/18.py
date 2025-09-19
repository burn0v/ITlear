fst = int(input('Введите число: '))
scn = int(input('Введите число: '))
type = str(input('Введите операцию (+, -, *, /): '))
if type == '+':
    print(fst + scn)
elif type == '-':
    print(fst - scn)
elif type == '*':
    print(fst * scn)
elif type == '/':
    print(fst / scn)
else:
    print('Ошибка, вы указали не верную операцию.')