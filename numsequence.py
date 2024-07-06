
print('--- Ascending Number Sequence Checker ---')

num = int(input('Input number: '))
numChecker = 0
Flag = True
i = 0

while num!=0:
    if num <= numChecker:
        Flag = False
    numChecker = num
    print(Flag)
    num = int(input('Input number: '))
    i+=1

if i < 2:
    Flag = False
print(Flag, " !!!")
