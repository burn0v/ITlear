list_sum = [1, 2, 3, 4, 5, 6]
summa = 0
exp = 1
for num in list_sum:
    summa += num
    exp *= num
print(summa, exp)