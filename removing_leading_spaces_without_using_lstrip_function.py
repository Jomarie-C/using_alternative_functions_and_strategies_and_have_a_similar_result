full_name = input("Enter your full name: ")
correct_format = ""
non_space_character = False

for char in full_name:
    if not non_space_character:
        if char != " ":
            non_space_character = True
            correct_format += char
    else:
        correct_format += char