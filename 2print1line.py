
while True:

    line_1 = input("Input line 1: ") 
    line_2 = input("Input line 2: ")

    print(line_1, end = " ")
    print(line_2)

    console = input('Wanna End ?? push E ')
    if console == 'e' or console == 'E':
        print('Program End !!')
        break