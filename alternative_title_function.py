input_string = input("Enter a string: ")
correct_format = ""

for char in range(len(input_string)):
    if char == 0 or input_string[char - 1] == " ":
        correct_format += input_string[char].upper()
    else:
        correct_format += input_string[char].lower()