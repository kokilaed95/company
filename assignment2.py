def get_sum_of_fibonacci(max_value):
    start_element, next_element = 1, 2
    sum_of_fibonacci = 0
    while(sum_of_fibonacci <= max_value):
        if next_element % 2 == 0:
            sum_of_fibonacci += next_element
        start_element, next_element = next_element, start_element + next_element
    return sum_of_fibonacci

print(get_sum_of_fibonacci(4000000))