userInput = input('Binary Number: ')
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
    print(str(int(userInput,2)))
else:
    print('This is not a valid binary number. please restart the program and try again')


