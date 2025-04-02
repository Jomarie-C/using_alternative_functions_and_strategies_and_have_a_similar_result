input_string = input("Enter a string: ")
uppercase = True

for char in input_string:
    if 'a' <= char <= 'z':
        uppercase = False
        break