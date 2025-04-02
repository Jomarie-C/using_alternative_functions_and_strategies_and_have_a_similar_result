input_string = input("Enter a string: ")
correct_format = True

for char in input_string:
    if 'a' <= char <= 'z':
        continue
    elif char.isalpha():
        correct_format = False
        break

if correct_format:
    print("All characters are lowercase.")
else:
    print("Not all characters are lowercase.")