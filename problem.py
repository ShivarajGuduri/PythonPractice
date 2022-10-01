#type = ["india", "china", "japan"]
india = ["idly", "wada", "sambar"]
china = ["sushi", "rawmen", "crab", "snake"]
japan = ["bread", "jam", "donut"]

dish = input("Enter the dish name : ")

if dish.lower() in india:
    print(f'{dish.title()} is an Indian Dish')
elif dish.lower() in china:
    print(f'{dish.title()} is an Chinese Dish')
elif dish.lower() in japan:
    print(f'{dish.title()} is an Japanese Dish')
else:
    print(f'{dish.title()} is not found in our menu')
