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

def intIntoBinary (number):
    validText = True
    for char in userInput:
        if not char.isnumeric():
            validText = False
            break
    if validText:
        number = "{0:b}".format(int(number))
        print(str(number))
        return number
    else:
        print('This is not a valid number. please restart the program and try again')
        return None


userInput = input('Number: ')
base = input('Base: ')
if base == '2':
    binaryIntoInt(userInput)
elif base == '10':
    intIntoBinary(userInput)
else:
    print('Incorrect setting')