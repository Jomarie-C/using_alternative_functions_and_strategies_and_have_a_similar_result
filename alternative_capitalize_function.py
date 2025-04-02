full_name = input("Enter your full name: ")
capitalized_name = ""

for char in range(len(full_name)):
    if char == 0:
        capitalized_name += full_name[char].isupper()
    else:
        capitalized_name += full_name[char].islower()