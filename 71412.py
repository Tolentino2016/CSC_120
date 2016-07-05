phoneNum = input("Enter a phone number to be translated:")

newPhoneNumber = '' 
for char in phoneNum:
    if char == 'A' or char == 'B' or char == 'C':
        char = '2'
    elif char == 'D' or char == 'E' or char == 'F':
        char = '3'
    elif char == 'G' or char == 'H' or char == 'I':
        char = '4'
    elif char == 'J' or char == 'K' or char == 'L':
        char = '5'
    elif char == 'M' or char == 'N' or char == 'O':
        char = '6'
    elif char == 'P' or char == 'Q' or char == 'R' or char == 'S':
        char = '7'
    elif char == 'T' or char == 'U' or char == 'V':
        char = '8'
    elif char == 'W' or char == 'X' or char == 'Y' or char == 'Z':
        char = '9'
    newPhoneNumber = newPhoneNumber + char

print(newPhoneNumber)
