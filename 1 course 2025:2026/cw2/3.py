list_main = [1, 2, 3, 4, 5, 6, 7, 8]
list_chet = []
for num in list_main:
    if num % 2 == 0:
        list_chet.append(num)
print(list_chet)