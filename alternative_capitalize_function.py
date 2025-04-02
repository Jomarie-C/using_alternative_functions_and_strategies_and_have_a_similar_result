full_name = input("Enter your full name: ")
capitalized_name = ""

for char in range(len(full_name)):
    if char == 0:
        capitalized_name += full_name[char].upper()
    else:
        capitalized_name += full_name[char].lower()

print("Output:", capitalized_name)