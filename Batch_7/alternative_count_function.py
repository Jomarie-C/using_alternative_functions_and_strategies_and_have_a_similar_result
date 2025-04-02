input_string = input("Enter a string: ")
substring = input("Enter the substring to count: ")
count = 0

for i in range(len(input_string) - len(substring) + 1):
    if input_string[i:i + len(substring)] == substring:
        count += 1

print("Output:", count)