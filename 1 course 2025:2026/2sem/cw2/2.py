def get_min_max(numbers):
    """
    Функция для нахождения миниимума и максимума в списках.
    
    Args:
        numbers (list): Список чисел.
    
    Returns:
        int: Максимальное и минимальное число из списка.
    """
    max_numbers = numbers[0]
    min_numbers = numbers[0]
    for num in numbers:
        if num > max_numbers:
            max_numbers = num
        if num < min_numbers:
            min_numbers = num
    return min_numbers, max_numbers


a = [3, 5, 1]
b = [10, 7, 12]
c = [4, 8, 6]

print(get_min_max(a))
print(get_min_max(b))
print(get_min_max(c))

def get_min_numbers(numbers):
    """
    Функция для нахождения миниимума в списках.
    
    Args:
        numbers (list): Список чисел.
    
    Returns:
        int: Минимальное число из списка.
    """
    min_numbers = numbers[0]
    for num in numbers:
        if num < min_numbers:
            min_numbers = num
    return min_numbers

def get_max_numbers(numbers):
    """
    Функция для нахождения максимума в списках.
    
    Args:
        numbers (list): Список чисел.
    
    Returns:
        int: Максимальное число из списка.
    """
    max_numbers = numbers[0]
    for num in numbers:
        if num > max_numbers:
            max_numbers = num
    return max_numbers

a = [3, 5, 1]
b = [10, 7, 12]
c = [4, 8, 6]

print(get_max_numbers(a))
print(get_min_numbers(a))