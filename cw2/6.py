numbers = [1, 2, 2, 3, 4, 5, 6, 6, 6]
unique = []
for num in numbers:
    if num not in unique:
        unique.append(num)
print(unique)
print(len(unique))