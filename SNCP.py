import math

print('Symmetric number checker program')

numInp = int(input('Input interger number need to check: '))

while numInp != 0:
    while numInp != 0 and (numInp < 1000 or numInp > 9999):
        numInp = int(input('Input interger number need to check: '))
    
    if math.floor(numInp/1000) == numInp%10 and math.floor((numInp%1000)/100) == math.floor(numInp%100/10):
        print('True')
    else:
        print('False')
    
    numInp = int(input('Input interger number need to check: '))
    