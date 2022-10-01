# function that takes a string and return a new string with all vowels removed

# given = "my name Is shivaraj"
# out = ""

# for char in given:
#     if char in "aeiouAEIOU":
#         continue
#     else:
#         out += char

# print(out)

def likes(names):
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return f"{names[0]} likes this"
    elif len(names) == 2:
        return f"{names[0]} and {names[1]} like this"
    elif len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {len(names)-2} others like this"


print(likes([]))
print(likes(['shiva']))
print(likes(['ramesh', "suresh"]))
print(likes(['raj', "ramesh", 'suresh']))
print(likes(['shiva', "raj", 'teja', 'vineet', "valli"]))
