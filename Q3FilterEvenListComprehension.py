# Question 3 - Use list comprehension to extract all of the even integers out of a list of integers
def filter_even_numbers(numbers):
    try:
        return [num for num in numbers if num % 2 == 0]
    except:
        return 'An exception occurred'

#Test 1 > Valid
numbers = [8, 7, 52, 11, 412]
even_numbers = filter_even_numbers(numbers)
print ('Even numbers in the input list: ', even_numbers)

# Test 2 > Valid
numbers = [2, 4, 89, 24, 63, 85, 10, 61]
even_numbers = filter_even_numbers(numbers)
print ('Even numbers in the input list: ', even_numbers)

# Test 3> Invalid
numbers = 'random'
even_numbers = filter_even_numbers(numbers)
print ('Even numbers in the input list: ', even_numbers)

# Test 4 > Valid but no even numbers in the list
numbers = [3, 7, 89, 25]
even_numbers = filter_even_numbers(numbers)
print ('Even numbers in the input list: ', even_numbers)