full_name = input("Enter your full name: ")
correct_format = ""

for char in input_string:
    if 'a' <= char <= 'z':  
        correct_format += chr(ord(char) - 32) 
    else:
        correct_format += char