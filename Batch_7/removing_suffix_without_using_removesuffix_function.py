input_string = input("Enter a string: ")
suffix = input("Enter the suffix to remove: ")

if input_string.endswith(suffix):
    input_string = input_string[:-len(suffix)]

print("Output:", input_string)