full_name = input("Enter your full name: ")
correct_format = ""

for char in full_name:
    if 'a' <= char <= 'z':  
        correct_format += chr(ord(char) - 32) 
    else:
        correct_format += char

print("Output:", correct_format)