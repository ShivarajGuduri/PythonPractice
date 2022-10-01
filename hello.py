def even_or_odd(number):
    # if number % 2 == 0:
    #     return ("even")
    # return ("odd")
    return 'Even' if (number % 2) == 0 else 'Odd'


print(even_or_odd(5))
print(even_or_odd(2))
print(even_or_odd(0))
print(even_or_odd(-5))
print(even_or_odd(-10))
