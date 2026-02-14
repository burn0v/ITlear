numbers = [1, -2, 3, -4, 5]


def is_positive(number):
    return number > 0

def sum_positive(numbers):
    positive_sum = 0
    for number in numbers:
        if is_positive(number):
            positive_sum += number
    return positive_sum

def count_positive(numbers):
    positive_count = 0
    for number in numbers:
        if is_positive(number):
            positive_count += 1
    return positive_count
        
print(sum_positive(numbers))
print(count_positive(numbers))



numbers = [1,2,3,4,5,6]


def is_even(number):
    return number % 2 == 0

def is_odd(number):
    return number % 2 != 0
    
def filter_even(numbers):
    even_numbers = []
    for number in numbers:
        if is_even(number):
            even_numbers.append(number)
    return even_numbers

def filter_odd(numbers):
    odd_numbers = []
    for number in numbers:
        if is_odd(number):
            odd_numbers.append(number)
    return odd_numbers

print(filter_even(numbers))
print(filter_odd(numbers))