input_string = input("Enter a string: ")
prefix = input("Enter the prefix to check: ")

if input_string[:len(prefix)] == prefix:
    print("The string starts with the given prefix.")
else:
    print("The string does not start with the given prefix.")