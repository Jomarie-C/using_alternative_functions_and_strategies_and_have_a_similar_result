input_string = input("Enter a string: ")
total_lenght = int(input("Enter the lenght: "))

alternative_ljust = input_string + ' ' * (total_lenght - len(input_string))
print("\nOutput:", alternative_ljust)