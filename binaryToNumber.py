def binaryIntoInt (number):
    validText = True
    for char in userInput:
        if not char.isnumeric():
            validText = False
            break
        else:
            intText = (int) (char)
            if not (intText == 0 or intText == 1):
                validText = False
                break
    if validText:
        number = int(userInput,2)
        print(str(number))
        return number
    else:
        print('This is not a valid binary number. please restart the program and try again')
        return None

userInput = input('Binary Number: ')
binaryIntoInt(userInput)