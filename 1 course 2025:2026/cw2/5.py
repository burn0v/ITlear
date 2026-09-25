# Поиск минимума и максимума
list_main = [1, 2, 30, -1, 5, 6, 123, 8, 92, 10]
min_index = max_index = 0
for num in list_main:
    if num < list_main[max_index]:
        max_index = num
    if num > list_main[min_index]:
        min_index = num 
print(max_index, min_index)
    