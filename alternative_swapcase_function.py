full_name = input("Enter your name: ")
reverse_casing = ""

for char in full_name:
    if char.islower():
        reverse_casing += char.upper()
    if char.isupper():
        reverse_casing += char.lower()

print("\nOutput:", reverse_casing)