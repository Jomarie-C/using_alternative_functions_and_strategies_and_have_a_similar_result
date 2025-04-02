input_string = input("Enter a string: ")
suffix = input("Enter the suffix you want to check: ")

if input_string[-len(suffix):] == suffix:
    print("\nOutput: The string ends with the suffix.")
else:
    print("\nOutput: The string does not end with the suffix.")