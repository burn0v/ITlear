fst_num = int(input('Введите число: '))
scn_num = int(input('Введите число: '))
if fst_num > scn_num:
    print(f'Число {fst_num} больше чем {scn_num}')
elif fst_num == scn_num:
    print(f'Число {fst_num} равно числу {scn_num}')
else:
    print(f'Число {scn_num} больше чем {fst_num}')
