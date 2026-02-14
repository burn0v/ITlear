def even_numbers(numbers):
    """Функция для подсчета четных чисел.
    
    Args: 
        numbers (list): Списко чисел.
    
    Returns:
        int: Колличество всех четных чисел.
    """
    count = 0
    for number in numbers:
        if number % 2 == 0:
            count += 1
    return count

def return_max_num(numbers):
    """
    Функция для возвращения максимального числа из списка.

    Args: 
        numbers (list): Список чисел.
    
    Returns:
        int: Максимальное число из списка.
    """
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

def get_doubled_threshold(numbers, threshold):
    """
   Фунция для возвращении списка чисел, больше порога, умноженных на 2.

   Args: 
        numbers (list): Список чисел.
        threshold (int): Пороговое значение.

    Returns: 
        int: Список чисел, больше порога, умноженных на 2.
    """
    value = []
    for number in numbers:
        if number > threshold:
            value.append(number * 2)
    return value

def get_longest_string(strings):
    """
    Функция для возвращения самой длинной строки из списка.
    
    Args:
        strings (list): Список строк.

    Returns:
        str: Самая длинная строка. 
    """
    longest_string = ""
    for current_string in strings:
        if len(current_string) > len(longest_string):
            longest_string = current_string
    return longest_string