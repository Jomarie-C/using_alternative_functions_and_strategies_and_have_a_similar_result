input_string = input("Enter a string: ")
correct_format = True

for char in input_string:
    if 'a' <= char <= 'z':
        continue
    elif char.isalpha():
        correct_format = False
        break