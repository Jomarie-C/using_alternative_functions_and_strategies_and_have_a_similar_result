num = int(input("Enter an integer: "))
lenght = int(input("Enter the lenght: "))

correct_format = f"{num:0>{lenght}}"

print("Output:", correct_format)