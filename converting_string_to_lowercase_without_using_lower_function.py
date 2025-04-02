name = input("Enter your name: ")
lower_casing = ""

if char in name:
    if "A" <= char <= "Z":
        lower_casing += chr(ord(char) + 32)
    else:
        lower_casing += char