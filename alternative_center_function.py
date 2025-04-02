input_string = input("Enter a string: ")
total_lenght = int(input("Enter the total lenght: "))

spaces = total_lenght - len(input_string)
left_spaces = ' ' * (spaces // 2)
right_spaces = ' ' * (spaces - len(left_spaces))
centered_text = left_spaces + input_string + right_spaces

print("\nOutput:", centered_text)