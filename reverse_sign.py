def opposite(number):
    try:
        number = number * -1
        return number
    except ValueError:
        print("Input data cannot be represented as a number")
        return None


print(opposite("a"))
