input_string = input("Enter a string: ")
substring = input("Enter the substring to find: ")

position = input_string.find(substring)

if position != -1:
    print(f"Found '{substring}' at index {position}.")
else:
    print(f"'{substring}' was not found.")