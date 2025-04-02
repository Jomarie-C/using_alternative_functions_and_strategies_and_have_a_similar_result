input_string = input("Enter a string: ")
total_length = int(input("Enter the total length: "))

if len(input_string) < total_length:
    spaces_needed = total_length - len(input_string)
    input_string = ' ' * spaces_needed + input_string

print("Output:", input_string)