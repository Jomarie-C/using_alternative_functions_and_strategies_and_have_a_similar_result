full_name = input("Enter your full name: ")

while full_name.endswith(' '):
    full_name = full_name[:-1]

print("Output:", full_name)