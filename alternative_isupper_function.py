input_string = input("Enter a string: ")
uppercase = True

for char in input_string:
    if 'a' <= char <= 'z':
        uppercase = False
        break

if uppercase:
    print("All characters are in uppercase.")
else:
    print("Not all characters are in uppercase.")