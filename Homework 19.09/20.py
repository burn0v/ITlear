maxn = 0
while True:
    enter_num = int(input("Введите чилсо: "))
    if enter_num == 0:
        print('Максимальное число:', maxn)
        break 
    if enter_num > maxn:
        maxn = enter_num
